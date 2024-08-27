import game_data as gd
import random
#Function to compare a and b
def compare(answer):
    global count
    global right
    if answer == 'A' and a_followers > b_followers:
        count += 1
        print(f"That's right! score: {count}\n\n")
    elif answer =='B' and b_followers > a_followers:
        count += 1
        print(f"That's right! score: {count}\n\n")
    else:
        print(f"Sorry, that's wrong.\n\n")
        right = False

#Generate first A and B
a_index = random.randint(0, len(gd.data) - 1)
b_index = random.randint(0, len(gd.data) - 1)

#Make sure you get diff values for both
if b_index ==  a_index:
    while b_index == a_index:
        b_index = random.randint(0, len(gd.data) - 1)

a_name = gd.data[a_index]['name']
b_name = gd.data[b_index]['name']

a_followers = gd.data[a_index]['follower_count']
b_followers = gd.data[b_index]['follower_count']

a_desc = gd.data[a_index]['description']
b_desc = gd.data[b_index]['description']

a_country = gd.data[a_index]['country']
b_country = gd.data[b_index]['country']


#Start a loop that continues until you're wrong
right = True
count = 0
while right == True:
    #Compare a to B
    print(f"Compare A: {a_name}, a {a_desc} from {a_country}\n---------------")
    print(f"Against B: {b_name}, a {b_desc} from {b_country}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    compare(answer)
    a_index = b_index
    b_index = random.randint(0, len(gd.data) - 1)
    if b_index ==  a_index:
        while b_index == a_index:
            b_index = random.randint(0, len(gd.data) - 1)

    a_name = gd.data[a_index]['name']
    b_name = gd.data[b_index]['name']

    a_followers = gd.data[a_index]['follower_count']
    b_followers = gd.data[b_index]['follower_count']

    a_desc = gd.data[a_index]['description']
    b_desc = gd.data[b_index]['description']

    a_country = gd.data[a_index]['country']
    b_country = gd.data[b_index]['country']

#Game over, print score 
print(f"Game over, final score: {count}")