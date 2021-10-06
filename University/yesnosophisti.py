# list of question
questions_list = ['האם חדשנות טובה לכלכלה? : ',
                  'האם וודגווד היה בעל מפעל לכלי חרס? : ',
                  'האם ניהול וטכנו זה מעפן? : ']
admin_answers_list = ['yes', 'yes', 'no']
user_answers_list = []
right_answers = []

for i in range(len(questions_list)):
    user_answers_list.append(input(questions_list[i]))
print(user_answers_list)
if user_answers_list[0] == admin_answers_list[0]:
    right_answers.append(1)

print(right_answers)