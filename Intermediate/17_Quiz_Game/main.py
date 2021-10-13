from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Holds list of questions
question_bank = []

# Retrieve the question and answer from data JSON, create question object and add to question bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Pass question bank to the QuizBrain class
quiz = QuizBrain(question_bank)

# Continue to get new question until all questions are asked
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
