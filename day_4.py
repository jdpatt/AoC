"""Advent of Code 2018 Day 4"""
from collections import defaultdict, Counter
from datetime import datetime
import operator
from re import search
from statistics import mode


def sort_guard_entries(text):
    """Read the input file in and transform the data into a sorted list."""
    with open(text, "r") as input_text:
        timelog = []
        for line in input_text:
            timelog.append(
                {
                    "time": datetime.strptime(line[:18], "[%Y-%m-%d %H:%M]"),
                    "action": line[19:],
                }
            )
    return sorted(timelog, key=operator.itemgetter("time"))


def record_guard_sleep_time(entries):
    """Loop through the entries and record sleep time for each id."""
    guard_log = defaultdict(list)
    current_id = 0
    start_sleep = None
    stop_sleep = None
    record_sleep = False
    for entry in entries:
        regex = search(r"(up)|(asleep)|#(\d+)", entry["action"])
        if not regex:
            raise ValueError(f"How'd we get here?: {entry['action']}")
        elif regex.group(1):  # Up
            stop_sleep = entry["time"].minute
            if current_id and record_sleep:
                for minute in range(start_sleep, stop_sleep):
                    guard_log[current_id].append(minute)
            record_sleep = False
        elif regex.group(2):  # Asleep
            start_sleep = entry["time"].minute
            record_sleep = True
        elif regex.group(3):  # ID
            current_id = int(regex.group(3))
    return guard_log


def find_the_laziest(log):
    """Give him a pink slip."""
    laziest = {"id": "Santa", "time": 0}
    for guard, minutes in log.items():
        sleep = len(minutes)
        if sleep > laziest["time"]:
            laziest["time"] = sleep
            laziest["id"] = guard
    return laziest["id"], mode(log[laziest["id"]])


def find_the_dependable_lazy(log):
    """Find the elf that is asleep the most times on the same minute."""
    entry = {"id": "Santa", "frequency": 0, "minute": 0}
    for elf, value in log.items():
        minute, frequency = Counter(value).most_common(1)[0]
        if frequency >= entry["frequency"]:
            entry["frequency"] = frequency
            entry["minute"] = minute
            entry["id"] = elf
    return entry["id"], entry["minute"], entry["frequency"]


if __name__ == "__main__":
    SORTED_ENTRIES = sort_guard_entries("input/input4.txt")
    LOG = record_guard_sleep_time(SORTED_ENTRIES)
    SLEEPY, TIME = find_the_laziest(LOG)
    print(f"Lazy ID: {SLEEPY} Minute: {TIME} -> {SLEEPY * TIME}")

    # Part 2
    ELF, MINUTE, _ = find_the_dependable_lazy(LOG)
    print(f"Dependable ID: {ELF} Minute: {MINUTE} -> {ELF * MINUTE}")
