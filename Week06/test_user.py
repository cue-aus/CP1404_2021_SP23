from user import *
user1 = User('Cue007')
print(user1)
user2 = User('Hellene', 5, 4)
print(user2)
user1.give_a_taco(user2)
print(user1)
print(user2)
# print(user1._semi_private) --> error
print(user1._User__super_private)


