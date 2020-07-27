from django.test import TestCase

# Create your tests here.

import pandas as pd

d = pd.read_excel('./words.xlsx')
df = pd.DataFrame(data=d).fillna('')

T = []
for row in df[:].itertuples():
	item = (getattr(row, '列1'), getattr(row, '列2'), getattr(row, '列3'))
	T.append(item)

print("loaded.")

""" let the label and mean splited """
""" i is the line in m """
# for i in m.split('\n'):
# 	label = i.split('.')[0][-2:]+'.'
# 	means = i.split('.')[1]
# 	print(label + ' -> ' + means)


# import pymysql
#
# db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='smile0217',use_unicode=True, db='PyDict', charset='utf8')
# cursor = db.cursor()
# sql = "insert into words(word, mean1, mean2)  VALUES (%s,%s,%s)"
# val = T
#
# try:
# 	print("Started.")
# 	cursor.executemany(sql, val)
# 	db.commit()
# except Exception as e:
# 	print(e)
# 	db.rollback()
#
# db.close()

