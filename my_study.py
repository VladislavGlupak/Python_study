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

