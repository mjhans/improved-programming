import re
import reprlib
from collections import Counter

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))
        
    def __repr__(self):
        return f"Senetence ({reprlib.repr(self.text)})"

file_path = "/home/mjhans/improved-programming/ch05-flow_control/Lorem.txt"

count_dict = Counter()
with open(file_path, "r") as fp:
    for line in fp:
        words = Sentence(line.lower())
        #words = re.split("[., \n]", line.lower())
        count_dict.update(words)

print(count_dict)

