from quiz_data import quiz_raw_data_list
from quiz_model import Question
from quiz_brain import Quiz

quiz_question_bank = []

#quiz_quesion_bank = [object question1, object quesion2,...]
for data in quiz_raw_data_list :
    que = data["question"]
    ans = data["correct_answer"]
    new_que = Question(que, ans)
    #object Question Attributes: question, answer
    quiz_question_bank.append(new_que)

my_quiz = Quiz(quiz_question_bank)

for quiz_que in quiz_question_bank :
    user_answer = input(f"\nQ.{my_quiz.q_num}/{my_quiz.total_q_num}:  {quiz_que.question} (True/False): ")
    if my_quiz.evaluate_user_answer(user_answer, quiz_que.answer) :
        print("Correct Answer.")
        my_quiz.score += 1
    else :
        print("Incorrect Answer.")    
    print(f"Correct answer was : {quiz_que.answer}")     
    print(f"Current score: {my_quiz.score}/{my_quiz.total_q_num}")   

print(f"\n      Quiz Over. Your score = {my_quiz.score}/{my_quiz.total_q_num}")





