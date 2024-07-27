class QuizBrain:

  def __init__(self, question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0


  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_anser = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_anser, current_question.answer)
  def check_answer(self, user_answer, question_answer):
    if user_answer.lower() == question_answer.lower():
      self.score += 1
    
      