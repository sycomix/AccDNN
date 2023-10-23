#!/usr/bin/env python

import sys
import argparse
import numpy as np

def compare(hex_file, int_file):
    # Parse the hex file
    data_list = []
    fp = open(hex_file, 'r')
    line_list = [line.strip() for line in fp]
    for s in line_list:
        data_line = [int(s[i:i+4], 16) for i in xrange(0, len(s), 4)]
        data_line.reverse()
        data_list.extend(data_line)
    int_array = np.array(data_list, dtype='float32')
    int_array[np.where(int_array >= 32768)] = int_array[np.where(int_array >= 32768)] - 65536

    data_str = ''.join('%d\n'%(data) for data in int_array)
    with open(int_file, 'w') as fd:
        fd.write(data_str)      
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Required arguments: input and output files.
    parser.add_argument(
        "hex_file",
        help="simulated results file."
    )
    parser.add_argument(
        "int_file",
        help="real results file."
    )
    # Optional arguments.
    args = parser.parse_args()

    compare(args.hex_file, args.int_file)

