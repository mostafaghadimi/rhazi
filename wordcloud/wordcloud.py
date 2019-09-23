from hazm import Normalizer, word_tokenize
import pandas as pd
import numpy as np

pd.options.display.max_rows
pd.set_option('display.max_colwidth', -1)

# Persian Stops Word List
with open('./persian-stops.txt', encoding='utf-8') as stop_file:
    stop_words = stop_file.read().splitlines()

# Reading input
excel_file = pd.read_excel(r'../files/consultationQuestionsـv2.xlsx')

question_data_frame = pd.DataFrame(excel_file)
question_data_frame = question_data_frame.applymap(str)

question_group = question_data_frame.astype({'expertise_id': float}).groupby('expertise_id')

question_join = question_group['question'].apply(' '.join)[1:]

question_sets = pd.DataFrame(question_join)

for index, question in question_sets.iterrows():
    normalizer = Normalizer()
    stemmer = Stemmer()
    normal_text = normalizer.normalize(str(question))
    word_list = word_tokenize(normal_text)
    stemmed_word_list = []
    for i in range(len(word_list)):
        stemmed_word_list[i] = stemmer.stem(word_list[i])
    new_word_list = []
    for i in range(len(stemmed_word_list)):
        # print(word_list[i])
        inserted = stemmed_word_list[i]
        for stop in stop_words:
            if stemmed_word_list[i] == stop:
                inserted = ""
        # print(inserted)
        new_word_list.append(inserted)

    text = " ".join(map(str, new_word_list))
    # print(text)
    with open(r'./output/{}.txt'.format(int(index)), 'w', encoding='utf-8') as file:
        # np.savetxt(file, text)
        file.write(text)
