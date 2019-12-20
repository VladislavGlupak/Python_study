# #Task attributes
#
#
# class BlogPost:
#     def __init__(self, user_name, text, number_of_likes):
#         self.user_name = user_name
#         self.text = text
#         self.number_of_likes = number_of_likes
#
#
# post1 = BlogPost(user_name="Maks",text="Post number 1",number_of_likes=10)
# post2 = BlogPost(user_name="Alex",text="Post number 2",number_of_likes=20)
#
# post1.number_of_likes = 30
#
# print(post1.number_of_likes)
# print(post2.number_of_likes)
#
# #Methods
#
#
# class BankAccount:
#     def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
#         self.client_id = client_id
#         self.client_first_name = client_first_name
#         self.client_last_name = client_last_name
#         self.balance = balance
#
#     def add(self, added_money):
#         self.balance = self.balance + added_money
#         print("Уважаемый " + self.client_first_name + " " + self.client_last_name + ". " + "Ваш положили " + str(self.balance))
#
#     def withdraw(self, withdraw_money):
#         self.balance = self.balance + withdraw_money
#         print("Уважаемый " + self.client_first_name + " " + self.client_last_name + ". " + "Вы сняли " + str(self.balance))
#
#
# Client1 = BankAccount(1, "Alex", "Nikitin")
# Client2 = BankAccount(2, "John", "Andreev")
#
# Client1.add(40)
# Client2.withdraw(50)
#
# # Inheritance. Polymorfism
#
#
# class GameCharacter:
#     def __init__(self, name, health, level):
#         self.name = name
#         self. health = health
#         self.level = level
#
#     def speak(self):
#         print("Hi, my name is " + self.name)
#
#
# class Villain(GameCharacter):
#     def __init__(self, name, health, level):
#         GameCharacter.__init__(self, name, health, level)
#
#     def speak(self):
#         print("Hi, my name is " + self.name + "and I will kill you")
#
#     def kill(self, who):
#         who.health = 0
#         print(who.name + "," + " " + "bang-bang, now you're dead")
#
#
# gamer1 = GameCharacter("Alex", 5, 3)
# gamer2 = Villain("John", 10, 5)
#
# gamer1.speak()
# gamer2.speak()
#
# print(gamer1.health)
# gamer2.kill(gamer1)
# print(gamer1.health)


# class Chain:
#     def __init__(self, number_of_items):
#         self.number_of_items = number_of_items
#
#     def __str__(self):
#         return 'Chain with' + ' ' + self.number_of_items + ' ' + 'items'
#
#     def __len__(self):
#         return self.number_of_items
#
#
# line = Chain('11')
#
# print(line.__str__())
# print(line.__len__())

import math

print(math.sqrt(123456789))
print(math.factorial(987))
print(math.pow(876,54))