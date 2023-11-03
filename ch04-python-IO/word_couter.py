import re

file_path = "Lorem.txt"
#count_dict = {}

# with open(file_path, "r") as fp:
#     for line in fp:
#         words = re.split("[., \n]", line.lower())
#         #print(words)
#         for word in words:
#             if word not in count_dict:
#                 count_dict[word] = 0
#             count_dict[word] += 1

from collections import Counter
count_dict = Counter()
with open(file_path, "r") as fp:
    for line in fp:
        words = re.split("[., \n]", line.lower())
        count_dict.update(words)

print(count_dict)

