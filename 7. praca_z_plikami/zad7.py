import json
from os import path

dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

words_list = []
with open(data_path, "r", encoding="utf-8") as f:
    file_lines = f.readlines()
for line in file_lines:
    words = line.split()
    words_list.extend(words)
print("liczba slow:" + str(len(words_list)))






        
    