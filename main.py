from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# #Text and answer key word is common in every line mere ko iteration se sirf no. ke sath khelna hai
question_bank = []

for i in range(0, len(question_data)):
    question_bank.append(Question(question_data[i]["question"], question_data[i]["correct_answer"]))

# print(question_bank[0].ques) --> Yeh isiliye banaya taaki pta chale ki kaam kr rha hai

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Okay!!! so there you completed your Quiz. And your final score is {quiz.score}/{len(question_bank)}")


