from lib import open_file

answers = open_file("6/input")
# For conveniance we add an empty string at the end of our answers
answers.append("")


def nb_questions_yes(group_answers, everyone=False):
    questions = {}
    for answers in group_answers:
        for answer in answers:
            if answer in questions.keys():
                questions[answer] += 1
            else:
                questions[answer] = 1
    if everyone:
        return sum(1 for answer in questions.keys() if questions[answer] == len(group_answers))
    else:
        return len(questions.keys())


res_anyone, res_everyone = 0, 0
group_answers = []
for answer in answers:
    if not answer:
        res_anyone += nb_questions_yes(group_answers)
        res_everyone += nb_questions_yes(group_answers, everyone=True)
        group_answers = []
    else:
        group_answers.append(answer)

print("### PART 1")
print(res_anyone)
print("### PART 2")
print(res_everyone)
