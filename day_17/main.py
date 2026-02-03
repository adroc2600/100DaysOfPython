from question_model import Question
from quiz_brain import QuizBrain
import requests
import html

api_url = 'https://opentdb.com/api.php?amount=10&type=boolean'
'''
results:[{'type': 'boolean', 'difficulty': 'hard', 'category': 'Science: Computers', 'question': 'DHCP stands for Dynamic Host Configuration Port.', 'correct_answer': 'False', 'incorrect_answers': ['True']}
'''

question_bank = []

response = requests.get(api_url)
#print(type(response))

response_json = response.json()
#print(type(response_json))

results = response_json["results"]
#print(type(results))

for item in results:
    question_bank.append(Question(html.unescape(item["question"]),item["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score is {quiz.score}/{quiz.question_number}")