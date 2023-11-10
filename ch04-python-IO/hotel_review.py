import csv
import re
import json

from collections import Counter

p_counter = Counter()
n_counter = Counter()

def word_maker(data):
    words = re.split("[., \n]", data.lower())
    return words

def file_write(file_path, file_name, data):
    with open(f"{file_path}/{file_name}", "w") as f:
        f.write(data)

FILE_NAME = "Hotel_Reviews.csv"
FILE_PATH = "/home/mjhans/improved-programming"
with open(f"{FILE_PATH}/{FILE_NAME}") as f:
    data = csv.DictReader(f, delimiter=",")
    for row in data:
        p_words = word_maker(row["Positive_Review"])
        p_counter.update(p_words)
        n_words = word_maker(row["Negative_Review"])
        n_counter.update(n_words)
#print(p_counter)
file_write(file_path=".", file_name="p_review.txt", data=json.dumps(p_counter))
file_write(file_path=".", file_name="n_review.txt", data=json.dumps(n_counter))



