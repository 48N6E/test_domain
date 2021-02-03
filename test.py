import os
import codecs

file_name = r'C:\\Users\\abc\\Downloads\\a.txt'
with codecs.open(file_name,encoding='utf-8') as file:
    lines = file.readlines()

row_count = 1
with codecs.open(file_name,'w',encoding='utf-8') as file:
    for line in lines:
        file.write("%-5d"% row_count + ':'+line)
        row_count+=1
