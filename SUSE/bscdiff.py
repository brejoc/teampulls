#! /usr/bin/env python2

__author__ = "Jochen Breuer <jbreuer@suse.de>"
__license__ = "MIT"
__version__ = "0.1"
__doc__ = """\
This script compares bsc numbers from a source changelog, to a target changelog.
Missing bsc numbers are then printed with their occurrence in the source
changelog.

Usage: bscscanner.py <source_file> <target_file>
"""

import sys
import re

# These are the patterns we are looking for.
PATTERNS = (r"bsc#\d*", r"U#\d*")

def extract_result_list_from_source(source_file):
    """
    Get results set, which looks like that: (line_count, bscs, line)
    """
    with open(source_file, 'r') as f:
        results = []
        line_count = 0
        for line in f:
            line_count += 1
            for pattern in PATTERNS:
                matches = re.findall(pattern, line)
                for match in matches:
                    results.append((line_count, match, line))
    return results

def extract_bscs(results):
    """
    Extract bscs from results list.
    """
    bscs = []
    for element in results:
        bscs.append(element[1])
    return list(set(bscs)) # filtering out the duplicates

def reduce_bscs(bscs, target_file):
    """
    Compare given bscs to bscs in target file.
    """
    with open(target_file, 'r') as f:
        for line in f:
            for bsc in bscs:
                if bsc in line:
                    bscs.remove(bsc)
    return bscs

def print_missing(missing_bscs, results):
    """
    Fetch missing bscs from result set.
    """
    for bsc in missing_bscs:
        for result in results:
            if bsc in result[1]:
                sys.stdout.write("missing {} from line {} -> {}".format(
                    bsc,
                    result[0],
                    result[2]))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("usage: {} <source_file> <target_file>".format(
            sys.argv[0]))
        sys.exit(1)
    source_file = sys.argv[1]
    target_file = sys.argv[2]

    results = extract_result_list_from_source(source_file)
    bscs = extract_bscs(results)
    missing_bscs = reduce_bscs(bscs, target_file)
    print_missing(missing_bscs, results)

