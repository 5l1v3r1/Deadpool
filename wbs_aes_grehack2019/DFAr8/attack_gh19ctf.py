#!/usr/bin/env python3

import sys
import os
import deadpool_dfa
import phoenixAES
import binascii
import random

def processinput(iblock, blocksize):
    p='%0*x' % (2*blocksize, iblock)
    return (None, [p])

def processoutput(output, blocksize):
    return int(output[:32], 16)


engine=deadpool_dfa.Acquisition(targetbin='./main', targetdata='./main', goldendata='main.gold',
        dfa=phoenixAES, processinput=processinput, processoutput=processoutput, maxleaf=128, minleaf=1, verbose=2, addresses=(0x30000, 0x40000), faults=[('xor4', lambda x: x ^ random.randint(1,0xF))])
tracefiles_sets=engine.run()
