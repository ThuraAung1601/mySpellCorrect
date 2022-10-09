# Written by Thura Aung
# 9 Oct 2022
# Statistical methods for Spelling Correction in Burmese language
# python ./mySpellCorrect.py -i test.txt 
# for help : python ./mySpellCorrect.py -h 

import os
import re
import string
import argparse

from ngram import NGram
from symspellpy.symspellpy import SymSpell
from symspellpy.editdistance import DistanceAlgorithm

parser = argparse.ArgumentParser(description='Statistical Spelling Correction for Burmese language')
parser.add_argument('-cp', '--corpus', type=str, default='./data/myPOS.word',help='corpus file for n-gram', required=False)
parser.add_argument('-ut', '--unigram_dict', type=str, default='./data/small_frequency_dictionary_mm',help='unigram frequency dictionary file', required=False)
parser.add_argument('-bt', '--bigram_dict', type=str, default='./data/small_frequency_bigram_dictionary_mm',help='bigram frequency dictionary file', required=False)

parser.add_argument('-i', '--input', type=str, help='input file', required=False)
parser.add_argument('-o', '--output', type=str, default='./corrected.txt', help='output file', required=False)

parser.add_argument('-m', '--mode', type=str, default=r's', help='s for symspell and n for n-gram spelling correction', required=False)

args = parser.parse_args()

inputFile = getattr(args, 'input')
outFile = getattr(args, 'output')

corpus_path = getattr(args,'corpus')
bigram_path = getattr(args,'bigram_dict')
dictionary_path = getattr(args, 'unigram_dict')

mode = getattr(args,'mode')

corpus = " ".join(open(corpus_path).read().splitlines())

def ngramSpell(sentences):
  '''
  sentences : input sentence
  '''
  n = 2 #n = n-gram, default is 2
  ngram = NGram(corpus.split(),N=n)
  predicts = []
  if not isinstance(sentences, list):
            sentences = [sentences]
            
  for i in range(len(sentences)):
            split = []

            for x in sentences[i].split():
                sugg = ngram.find(x) if x not in string.punctuation else None
                split.append(sugg if sugg else x)

            predicts.append(" ".join(split))
  return predicts

def mySymSpell(sentences):
  '''
  sentences = input sentence
  '''
  distance = 3 #maximum edit distance
  symspell = SymSpell(max_dictionary_edit_distance=distance)
  symspell._distance_algorithm = DistanceAlgorithm.DAMERAU_OSA_FAST
  
  symspell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)
  
  symspell.load_dictionary(dictionary_path, term_index=0, count_index=1)
  
  predicts = []

  # Word Segmentation using SymSpell
  #sentences = symspell.word_segmentation(sentences, 0)[0]

  if not isinstance(sentences, list):
        sentences = [sentences]

  for i in range(len(sentences)):
            split = []

            for x in sentences[i].split():
                sugg = symspell.lookup(x, verbosity=0, max_edit_distance=distance,
                                       transfer_casing=True) if x not in string.punctuation else None
                split.append(sugg[0].term if sugg else x)

            predicts.append(" ".join(split))

  return predicts


def main():

  data = ""
  with open(inputFile, encoding='utf-8') as file:
      for line in file:
        if mode=='s':
          corrected = mySymSpell(line)
          corrected = str(corrected[0])
        elif mode=='n':
          corrected = ngramSpell(line)
          corrected = str(corrected[0])
        data += corrected + "\n"
         
  if outFile:
    try:
      with open(outFile, 'w',  encoding='utf-8') as file:
      
         file.write(data)
      print(f"Spelling Correction succcessfully done. Write data to {outFile}")
    except:
      exit('Output file cannot be opened!')
	
	
if __name__ == "__main__":
    main ()

