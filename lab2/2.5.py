# -*- coding: utf-8 -*-
import jieba 
from collections import Counter
fp=open("三国演义.txt","r")
s=fp.read()
ct=jieba.cut(s)

c = Counter(ct).most_common(20)

print(c)

