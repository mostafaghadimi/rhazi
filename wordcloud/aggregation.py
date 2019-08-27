import pandas as pd
import numpy as np

excel_file = pd.read_excel(r'../files/consultationQuestionsـv2.xlsx')

question_data_frame = pd.DataFrame(excel_file)
question_data_frame = question_data_frame.applymap(str)

question_group = question_data_frame.astype({'expertise_id': float}).groupby('expertise_id')

question_join = question_group['question'].apply(' '.join)[1:]

question_sets = pd.DataFrame(question_join)

for index, question in question_sets.iterrows():
    with open(r'./input/{}.txt'.format(int(index)), 'w', encoding='utf-8') as file:
        np.savetxt(file, question, fmt="%s")