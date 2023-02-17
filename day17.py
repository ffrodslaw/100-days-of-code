# Day 17
# Creating you own classes

#####################################

class User:  # convention: PascalCase
    pass


user_1 = User()
user_1.id = "001" # add attribute
user_1.username = "anna"

print(user_1.username)

# special function __init__ is used for construction of the class

class User:

    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0 # default attribute
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "anna")
user_2 = User("002", "francis")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

