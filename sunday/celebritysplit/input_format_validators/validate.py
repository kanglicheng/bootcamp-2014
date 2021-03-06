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

while True:
    line = stdin.readline()
    assert oneint.match(line)
    n = int(line)
    if n == 0:
        break
    assert 1 <= n <= 24

    for i in range(n):
        line = stdin.readline()
        assert oneint.match(line)
        a = int(line)
        assert 1 <= a <= 4 * 10 ** 7

assert len(stdin.readline()) == 0
sys.exit(42)
