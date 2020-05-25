#!/usr/bin/python
# -*- coding: UTF-8 -*-
f1 = open(r"F:\2020研一下学期hufuping\xdl\LungCancer_result09.txt")
f2 = open(r"F:\2020研一下学期hufuping\xdl\SkinCancer_result09.txt")
file1_raw = f1.read()
file2_raw = f2.read()
file1_words = file1_raw.split()
file2_words = file2_raw.split()
result = set(file1_words).difference(set(file2_words))   #在file1中不在file2中
#print(result)
for w in file2_words:
    file1_raw = file1_raw.replace(w,"")
print(file1_raw)