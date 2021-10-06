import pandas as pd
# from sklearn import linear_model
# import csv
# from sklearn.preprocessing import Binarizer
# import ast

df = pd.read_csv('txt_to_understand.txt', delimiter="\t")  # a is the file name

print(df)
                         # לחלק את הדאטה למילים לאותיות למספרים, לתת לכל מילה מספר, לעשות חלוקה לפי משקל, מקום במילון, כמות פעמים שהשתמשו בה
                         # [  0    1   2   3   4  5   6       7    ]
    #                      [אין דברי תורה מתקיימים אלא במי שממית עצמו עליהם מלך מלכי המלכים הקדוש ברוך הוא אתה נתת אתה בראתה אתה נפחתה בי ואתה משמרה בקרבי ואתה עתיד לטלה ממני בכל זמן שעתיד לבוא]
    # greetings_words_list [1      0   0   0   0  0   0     0 ]
    # body_name_list       [0      1   0   0   0  1   0     0 ]
    #                      [0      0   1   0   0  0   0     0 ]
    #                      [0      0   0   1   0  0   0     0 ]
    #                      [0      0   0   0   1  0   0     0 ]
    #                      [0      0   0   0   0  1   0     0 ]
    #                      [0      0   0   0   0  0   1     0 ]
    #                      [0      0   0   0   0  0   0     1 ]
if index 1 in bodyname_binary and bodyname_reg:
    return True