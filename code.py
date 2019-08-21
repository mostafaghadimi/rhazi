import pandas as pd

dataframe = pd.read_csv(r'./files/98.5.29-consultationQuestions.csv')
print(unicode(dataframe).decode('utf-8'))
# print(dataframe)
# dataframe.head()
# print(dataframe)