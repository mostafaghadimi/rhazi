import pandas as pd


def question_category_count(categories, counts):
    length = len(categories)
    q_info = dict()

    for i in range(length):
        q_info[categories[i]] = counts[i]

    return q_info

pd.set_option('display.expand_frame_repr', False)


questions_file = pd.read_excel(r'./files/consultationQuestionsـv2.xlsx')

questions_data_frame = pd.DataFrame(questions_file)

categories_file = pd.read_excel(r'./files/medicalSections.xlsx')
categories_data_frame = pd.DataFrame(categories_file)["medicalSections"]

categories = []
for i in categories_data_frame:
    categories.append(i)

medical_section = questions_data_frame["medicalSection_id"].fillna(0.0).astype(int)
count_sections = [0 for _ in range(51)]

for id in medical_section:
    if id:
        count_sections[id] += 1
count_sections = count_sections[1:] + [0]

q_info = question_category_count(categories, count_sections)
print(q_info)




