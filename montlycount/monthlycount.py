import pandas as pd
import numpy as np

excel_file = pd.read_excel(r'../files/consultationQuestionsـv2.xlsx')
questions_data_frame = pd.DataFrame(excel_file, columns=["medicalSection_id", "created"])

time_intervals = pd.period_range(start="2014-04", end="2019-08", freq="M")
medical_id = np.array(range(1,52))

monthly_data_frame = pd.DataFrame({'count': 0}, index= time_intervals, columns=medical_id)
monthly_data_frame = monthly_data_frame.fillna(0).astype(int)

for index, row in questions_data_frame.head().iterrows():
    monthly_data_frame.loc[row['created'][:7], row["medicalSection_id"]] += 1

print(monthly_data_frame)