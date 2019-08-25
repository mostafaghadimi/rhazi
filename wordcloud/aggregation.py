import pandas as pd

excel_file = pd.read_excel(r'../files/consultationQuestionsـv2.xlsx')

question_dataframe = pd.DataFrame(excel_file)
question_dataframe = question_dataframe.applymap(str)

question_group = question_dataframe.groupby('medicalSection_id')

question_join = question_group['question'].apply(' '.join)

print(question_join)