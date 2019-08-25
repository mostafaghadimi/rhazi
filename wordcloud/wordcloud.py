from hazm import Normalizer
import re

with open('persian-stops.txt', encoding='utf-8') as stop_file:
    stop_words = stop_file.read().splitlines()
    print(stop_words)

with open('input.txt', encoding='utf-8') as input_file:
    input_text = ""
    normalizer = Normalizer()
    for line in input_file:
        input_text += normalizer.normalize(line)

with open('output.txt', 'w', encoding='utf-8') as output_file:
    for line in input_text:
        for stop_word in stop_words:
            if re.compile(r"\b" + stop_word + r"\b").findall(line):
                line = line.replace(stop_word, "")
        output_file.write(line)

#test = "چت سیاسی"
# for stops in stop_words:
#     if (re.compile(r"\b" + stops + r"\b").findall(test)):
#         test = test.replace(stops, "")
# print(test)