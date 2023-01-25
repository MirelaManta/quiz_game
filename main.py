from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    new_question = Question(questions["text"], questions["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

else:
    print("You've completed the quiz")
    print(f"Your final score is {quiz.score}/{quiz.question_number}")