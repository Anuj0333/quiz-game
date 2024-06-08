import quiz_brain
from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
quiz=quiz_brain.Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()


print("you completed the quiz successfully")
print(f"your final score was {quiz.score}/{quiz.question_number} ")
