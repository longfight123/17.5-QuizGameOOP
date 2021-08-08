from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for a_question in question_data:
    question_bank.append(Question(a_question['text'], a_question['answer']))

quiz_brain = QuizBrain(question_bank)
while quiz_brain.questions_remaining():
    quiz_brain.next_question()

