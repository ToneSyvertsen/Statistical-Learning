#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:35:49 2017

@author: tonesyvertsen
"""

import nltk
nltk.download()


 entries = nltk.corpus.cmudict.entries()
 all_words = [e[0] for e in entries]
 distinct_words = set(all_words)
 counts = FreqDist(all_words)
 polypron_words = [c for c in all_words if counts[c] > 1]
 final_fraction = len(polypron_words) / len(distinct_words)
 print ("The CMU pronuncing dictionary contains %i distinct_words" % len(distinct_words))
 print ("The fraction of words in this dictionnary which have",)
 print (" more than one possible pronunciation is %f" % final_fraction )   
  
  
import nltk
from nltk.corpus import cmudict
pron = cmudict.dict()

multi_pronunciation_word_ct = 0
word_ct = 0

for word in pron:
   word_ct += 1
   if len(pron[word]) > 1:
      multi_pronunciation_word_ct += 1
  
 print ('%2.2f%% of the %d words in the dictionary have multiple pronunciations' % ((float(multi_pronunciation_word_ct)*100)/word_ct,word_ct)

 nb_syn = sum(1 for _ in wn.all_synsets('n'))
 fac = len([s for s in wn.all_synsets('n') if len(s.hyponyms()) == 0]) / nb_syn * 100
 print ("The percentage of noun synsets with no hyponyms is %f" % fac)

wn.all_synsets('n')
