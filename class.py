class User : 

    def __init__(self, id, name) :
        self.user_id = id
        self.user_name = name
        print(f"Object created. id= {self.user_id}, name= {self.user_name}")
        self.followers = 0
        self.following = 0

    
    def follow(self, user) :
        self.following += 1
        user.followers += 1
            
    def print(self) :
        print(f"id={self.user_id}, name={self.user_name}, followers ={self.followers}, following ={self.following}")
        self.print1()

    def print1(self) :
        print("print1")     


user_1 = User("101", "John")
user_2 = User("102", "kennedy")
user_1.follow(user_2)
user_1.print()
user_2.print()
