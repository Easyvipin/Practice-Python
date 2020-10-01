# wap for charachter count.

import pprint
# module for printing dic look more understandable
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for charachter in message:
    count.setdefault(charachter, 0)
    count[charachter] = count[charachter] + 1

pprint.pprint(count)

""" count: -{
         : 13,
        ,: 1,
        .: 1,
        A: 1,
        I: 1,
        a: 4,
        b: 1,
        c: 3,
        d: 3,
        e: 5,
        g: 2,
        h: 3,
        i: 6,
        k: 2,
        l: 3,
        n: 4,
        o: 2,
        p: 1,
        r: 5,
        s: 3,
        t: 6,
        w: 2,
        y: 1
    }, """
