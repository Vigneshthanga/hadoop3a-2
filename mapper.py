#!/usr/bin/env python
"""mapper.py"""

import sys
rc =0
val=0
cc = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if (rc == 0):
        rc+=1
        continue
    # split the line into words
    cc = 0
    words = line.split(',')

    for word in words:
        #Column Index of GRADES_9_12_G
        if (cc == 19):
            #The word can be Null as well
            if (word):
                val = float(word)

        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        #we write the value itself and reducer will counting the number of lines
                if (10000 < val < 20000):
                    print(val)
            break
        cc += 1

