#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import shutil
import asciiplotlib as apl

def main():
    cols, rows = shutil.get_terminal_size((80, 20))
    y = [float(l) for l in sys.stdin.readlines()]
    x = list((range(1, len(y)+1)))
    fig = apl.figure()
    fig.plot(x, y, width=cols, height=rows)
    fig.show()

if __name__ == '__main__':
    main()
