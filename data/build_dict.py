"""
Python program to build unigram and bigram frequency dictionaries
How to run : python build_dict.py -i ur_corpus.txt
Original program : https://github.com/ye-kyaw-thu/myWord/blob/main/word_dict.py
modified by Thura Aung
"""

import os
import sys
import tempfile
import numpy as np
from collections import defaultdict
from pylab import *
import pickle
import math
import functools

# line 20 21 22 23 are added by Thura 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, help='input file', required=True)
args = parser.parse_args()
inputFile = getattr(args, 'input')

sys.setrecursionlimit(10**6)
# recursion limit added by Ye.

# from line 29 to line 41, 2 functions added by Thura
def convertTupleBI(tup):
        # initialize an empty string
    str1 = ''
    for item in tup:
        str1 = str1 + " " + item
    return str1

def convertTupleUNI(tup):
        # initialize an empty string
    str1 = ''
    for item in tup:
        str1 = str1 + item
    return str1

def count_bigram (file, bigram_dict_txt):
    fileBI_txt = open(bigram_dict_txt, "w")
    bigram  = defaultdict (int)
    with open (file, 'r') as fh:
        for line in fh:
            words = line.rstrip('\n').split()
            if len(words) > 0:
                pword = words[0]
                for word in words[1:]:
                    bigram[(pword,word)] += 1
                    pword = word
    for key, value in bigram.items():
    	# fileBI_txt.write (str(key)+'\t'+str(value)+'\n')
    	
    	# line 55 and 56 are added by Thura
    	key = convertTupleBI(key)
    	fileBI_txt.write (f"{key} {value}\n")

    fileBI_txt.close()
    
    # commented by Thura from line 63 to line 68
    # write binary dictionary
    # fileBI_bin = open(bigram_dict_bin, "wb")
    # pickle.dump(bigram, fileBI_bin)
    # fileBI_bin.close()            
    return bigram

def count_unigram (file, unigram_dict_txt):
    fileUNI_txt = open(unigram_dict_txt, "w")
    unigram = defaultdict (int)
    with open (file, 'r') as fh:
        for line in fh:
            words = line.rstrip('\n').split()
            for word in words:
                unigram[word] += 1
    for key, value in unigram.items():
    	#fileUNI_txt.write (str(key)+'\t'+str(value)+'\n')
        
        # line 78 and 79 are added by Thura
        key = convertTupleUNI(key)
        fileUNI_txt.write (f"{key} {value}\n")
        
    fileUNI_txt.close()
        
    # commented by Thura from line 88 to line 91
    # write binary dictionary
    # fileUNI_bin = open(unigram_dict_bin, "wb")    
    # pickle.dump(unigram, fileUNI_bin)
    # fileUNI_bin.close()        
    
    return unigram

# main function added by Thura
def main():
    file = inputFile
    bigram_dict_txt = "small_frequency_bigram_dictionary_mm"
    unigram_dict_txt = "small_frequency_dictionary_mm"
    count_bigram (file, bigram_dict_txt)
    count_unigram (file, unigram_dict_txt)

main()
