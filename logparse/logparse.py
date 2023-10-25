#!/usr/bin/env python3
""" log parser

    Tags:
    Generator function
    File Open/Close
    File parsing
    Datetime diff

    Accepts a filename on the command line.  The file is a linux-like log file
    from a system you are debugging.  Mixed in among the various statements are
    messages indicating the state of the device.  They look like:
        Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON
    The device state message has many possible values, but this program only
    cares about three: ON, OFF, and ERR.

    Your program will parse the given log file and print out a report giving
    how long the device was ON, and the time stamp of any ERR conditions.
"""

import datetime
import sys

def get_next_event(filename):
    """
    Retrieves the relevant data from the logfile
    Opens a file in the 'with' statement
    Uses a generator by calling 'yield'. The file will close after the final generated response
    Filters contents within the 'with' block to avoiding storing unneeded strings
    """
    with open(filename, "r") as datafile:
        for line in datafile:
            if "dut: Device State: " in line:
                line = line.strip()
                # Parse out the action and timestamp
                action = line.split()[-1]
                timestamp = line[:19]
                yield (action, timestamp)

def compute_time_diff_seconds(start, end):
    """
    Parses the timestamp string using the provided format and
    calculates the difference betwee the two times in seconds
    """
    format = "%b %d %H:%M:%S:%f"
    start_time = datetime.datetime.strptime(start, format)
    end_time = datetime.datetime.strptime(end, format)
    return (end_time - start_time).total_seconds()

def extract_data(filename):
    time_on_started = None
    errs = []
    total_time_on = 0

    for action, timestamp in get_next_event(filename):
        # First test for errs
        if "ERR" == action:
            errs.append(timestamp)
        elif ("ON" == action) and (not time_on_started):
            time_on_started = timestamp
        elif ("OFF" == action) and time_on_started:
            time_on = compute_time_diff_seconds(time_on_started, timestamp)
            total_time_on += time_on
            time_on_started = None
    return total_time_on, errs

if __name__ == "__main__":
    # filename provided by command line argument
    total_time_on, errs = extract_data(sys.argv[1])
    print(f"Device was on for {total_time_on} seconds")
    if errs:
        print("Timestamps of error events:")
        for err in errs:
            print(f"\t{err}")
    else:
        print("No error events found.")