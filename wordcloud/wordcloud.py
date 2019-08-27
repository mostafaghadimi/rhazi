from hazm import Normalizer, word_tokenize

with open('persian-stops.txt', encoding='utf-8') as stop_file:
    stop_words = stop_file.read().splitlines()

with open(r'./input/input.txt', encoding='utf-8') as input_file:
    input_text = []
    normalizer = Normalizer()
    for line in input_file:
        normal_line = normalizer.normalize(line)
        word_list = word_tokenize(normal_line)
        input_text.extend(word_list)

with open('output.txt', 'w', encoding='utf-8') as output_file:
    number_of_words = len(input_text)
    for i in range(number_of_words):
        for stop_word in stop_words:
            if input_text[i] == stop_word:
                input_text[i] = ""

# remove empty strings
input_text = list(filter(None, input_text))

print(input_text)



#test = "چت سیاسی"
# for stops in stop_words:
#     if (re.compile(r"\b" + stops + r"\b").findall(test)):
#         test = test.replace(stops, "")
# print(test)