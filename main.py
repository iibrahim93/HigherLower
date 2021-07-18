#Import the game_data
from replit import clear
import random
import game_data
import art
insta_users = game_data.data
vs = art.vs
logo = art.logo
print(logo)
#print(insta_users[0])
#Create a randomize function and pass in the dictionary
def compare(a_list,b_list):
    """ 
    Compare function accepts two list
    """
    if a_list['follower_count'] > b_list['follower_count']:
        answer = 'A'
    elif b_list['follower_count'] > a_list['follower_count']:
        answer = 'B'
    return answer

def random_insta_user(list_of_insta_user):
    """ 
    This function returns a random instagram user
    """
    random_user = random.choice(list_of_insta_user)
    
    return random_user
#Call the randomize function 
q= True
compare_a=random_insta_user(insta_users)


user_score = 0
while q:
    
    against_b=random_insta_user(insta_users)
    info_one_user = f"{compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}"
    info_two_user = f"{against_b['name']}, a {against_b['description']}, from {against_b['country']}"
    #Define the variables A & B (A: first follower, B:Second follower)

    print(f"Compare A: {info_one_user} \n")
    print(vs)
    print(f"Against_B: {info_two_user} \n")
        #Ask the user a question: who has more followers 
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    compare_check = compare(compare_a,against_b)
    if compare_check == user_input:
        user_score+=1
        # new_random=random_insta_user(insta_users)
        compare_a = against_b
        clear()
        print(logo)
        print(f"You're correct. Your current score is: {user_score}" )
        # against_b = new_random
    else:
        print(f"Sorry, end of game!! You finised with {user_score}")
        q=False
        break
