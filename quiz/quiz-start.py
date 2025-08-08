class Question :
    def __init__(self, qns, ans) :
        self.question = qns
        self.answer = ans


new_q = Question("Modi is the PM ?", "True")        
print(new_q.answer)