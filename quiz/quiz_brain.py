class Quiz :
    def __init__(self, q_bank) :
        
        self.score = 0 
        self.q_num = 1
        self.total_q_num = len(q_bank)

    def evaluate_user_answer(self, user_ans, correct_ans) :    
        self.q_num  += 1
        user_answer = user_ans.lower()
        return user_ans == correct_ans


