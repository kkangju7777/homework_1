#! /usr/bin/python3
import sys

cnt = 0

with open(sys.argv[1]) as handle:
    for line in handle:
        line = line.strip()
        if line.startswith('>'):
            continue
        cnt += len(line)
print(cnt)

