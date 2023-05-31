import json
from os import path
from typing import Dict
import string

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

endings: Dict[str, int] = {}

for word in words_list:
    cleaned_word = word.strip(string.punctuation)
    if cleaned_word:
        last_letter = cleaned_word[-1]
        if last_letter in endings:
            endings[last_letter] += 1
        else:
            endings[last_letter] = 1

print("Statystyki końcówek słów:")
print(json.dumps(endings, indent=4))




        
    