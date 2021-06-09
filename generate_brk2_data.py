#!/usr/bin/env python3
#
"""generate_brk2_data.py
Reads in two files:
 - list of cusips
 - breakdown structure
Writes SQL for populating brk2 table
"""
import argparse
import csv
import logging

import sys


def parse_args(argv):
    parser = argparse.ArgumentParser(prog=__file__, add_help=True)
    parser.add_argument("--cusip_file", help="cusip file", required=True, type=argparse.FileType('r'))
    parser.add_argument("--breakdown_file", help="breakdown file", required=True, type=argparse.FileType('r'))
    return parser.parse_args(argv)


def main(argv):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Here we go")
    args = parse_args(argv)
    try:
        process(args)
    finally:
        args.cusip_file.close()
        args.breakdown_file.close()
    return 0


def print_insert_lines(cusip, sectors):
    for ii in range(len(sectors)):
        print(f"insert into dbo.brk2 values('4P', '{cusip}', '{'.'.join(sectors[0:ii+1])}', {ii+1})\ngo")


def process(args):
    # breakdown
    breakdown_file_reader = csv.reader(args.breakdown_file, delimiter="\t")
    next(breakdown_file_reader)  # skip the headers
    breakdown_list = list(breakdown_file_reader)  # limit wiht [:2]
    # cusips
    cusip_file_reader = csv.reader(args.cusip_file)
    next(cusip_file_reader)  # skip the headers
    cusip_list = [item for sublist in cusip_file_reader for item in sublist]  # limit with [:5]
    for ii in range(len(cusip_list)):
        print_insert_lines(cusip_list[ii], breakdown_list[ii % len(breakdown_list)])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
