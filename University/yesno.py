names_list = []
answers_list = []
name = input("Full name: ")
names_list.append(name)
right_answers = []
wrong_answers = []
not_a_yn_answer = []
num_of_question = []


class one:
    answer = input("האם חדשנות טובה לכלכלה? : ")
    num_of_question.append(1)
    if answer == "yes":
        right_answers.append(1)
    elif answer == "no":
        wrong_answers.append('class one')
    else:
        not_a_yn_answer.append('class one')
    answers_list.append(answer)


class two:
    answer = input("האם וודגווד היה בעל מפעל לכלי חרס? : ")
    num_of_question.append(1)
    if answer == "yes":
        right_answers.append(1)
    elif answer == "no":
        wrong_answers.append('class two')
    else:
        not_a_yn_answer.append('class two')
    answers_list.append(answer)


print(name + " you were right on", str(sum(right_answers)) + "/" + str(sum(num_of_question)))
