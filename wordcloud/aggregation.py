import pandas as pd
import numpy as np

excel_file = pd.read_excel(r'../files/consultationQuestionsـv2.xlsx')

question_data_frame = pd.DataFrame(excel_file)
question_data_frame = question_data_frame.applymap(str)

question_group = question_data_frame.astype({'medicalSection_id': float}).groupby('medicalSection_id')

question_join = question_group['question'].apply(' '.join)

print(question_join[1:])
# for i in question_group:
# print(question_group.question.head())
# np.savetxt(r'./groupby/test.txt', question_join, fmt="%s", encoding='utf-8')
# for i in range(1, 49):
#     np.savetxt(r'./groupby/{}.txt'.format(i))

# for (i) in question_join:
#     print(i)



# with open('test.txt', 'w', encoding='utf-8') as test:
#     test.write(str(question_join))

# print(question_join)