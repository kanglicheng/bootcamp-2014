#!/usr/bin/env python3
from sys import stdin
import re
import sys

integer = "(0|-?[1-9]\d*)"
floating = integer + "?(\.\d+)?"
oneint = re.compile(integer + "\n")
twoint = re.compile(integer + " " + integer + "\n")
threeint = re.compile("(" + integer + " ){2}" + integer + "\n")
fourint = re.compile("(" + integer + " ){3}" + integer + "\n")
manyint = re.compile("(" + integer + " )*" + integer + "\n")
string = re.compile("[a-z]+\n")

line = stdin.readline()
assert oneint.match(line)
k = int(line)

for test in range(k):
    line = stdin.readline()
    assert oneint.match(line)
    n = int(line)
    assert 1 <= n <= 1000000
    line = stdin.readline()
    assert manyint.match(line)
    perm = sorted(map(int, line.split()))
    assert all(x==i+1 for i,x in enumerate(perm))

assert len(stdin.readline()) == 0
sys.exit(42)
