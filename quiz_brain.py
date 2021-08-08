class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_answer = None

    def next_question(self):
        self.current_answer = input(f'Q.{self.question_number}. {self.question_list[self.question_number].question}.'
                                    f' True or False?')
        self.check_answer()
        self.question_number += 1

    def questions_remaining(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def check_answer(self):
        if self.current_answer == self.question_list[self.question_number].answer:
            print(f'You got it! The answer is {self.question_list[self.question_number].answer}')
        else:
            print(f'Sorry the answer is {self.question_list[self.question_number].answer}')