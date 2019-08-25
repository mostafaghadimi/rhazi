import pandas as pd


pd.set_option('display.expand_frame_repr', False)

dataframe = pd.read_excel(r'./files/consultationQuestionsـv2.xlsx')

df = pd.DataFrame(dataframe)

medical_section = df["medicalSection_id"].fillna(0.0).astype(int)
count_sections = [0 for _ in range(51)]



for id in medical_section:
    if id:
        count_sections[id] += 1

print(count_sections)


# print(dataframe)

# for id in dataframe.iterrows():
    # print(id.split(" "))