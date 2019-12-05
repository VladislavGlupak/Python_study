#Task attributes

class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes

post1 = BlogPost(user_name="Maks",text="Post number 1",number_of_likes=10)
post2 = BlogPost(user_name="Alex",text="Post number 2",number_of_likes=20)

post1.number_of_likes = 30

print(post1.number_of_likes)
print(post2.number_of_likes)

#Methods

class BankAccount:
    def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def add(self, added_money):
        self.balance = self.balance + added_money
        print("Уважаемый " + self.client_first_name + " " + self.client_last_name + ". " + "Ваш положили " + str(self.balance))

    def withdraw(self, withdraw_money):
        self.balance = self.balance + withdraw_money
        print("Уважаемый " + self.client_first_name + " " + self.client_last_name + ". " + "Вы сняли " + str(self.balance))


Client1 = BankAccount(1, "Alex", "Nikitin")
Client2 = BankAccount(2, "John", "Andreev")

Client1.add(40)
Client2.withdraw(50)






