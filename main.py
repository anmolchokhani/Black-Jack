import random

all_numbers= []
for i in range(2,11):
    all_numbers.append(i)

all_numbers.extend([11,10,10,10])



    



def check_ace(total):
    if total<21:
        return 11
    else: 
        return 1


def dealing_user_card():
    users_cards = random.sample(all_numbers,2)
    total_user_value= users_cards[0]  + users_cards[1]
    if total_user_value == 21:
        return total_user_value
    print(f"Your cards are {users_cards} and your current score is {total_user_value}")

    while True:
        if total_user_value > 21: 
            return total_user_value 
        users_choice_after_initial = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if users_choice_after_initial == 'n':
            print(f"Your cards are {users_cards} and final score is {total_user_value}")    
            return total_user_value
        t= random.choice(all_numbers)
        if t == 11:  
            t=check_ace(total_user_value+ t)
        users_cards.append(t)
        total_user_value += t
        print(f"Your cards are {users_cards} and your current score is {total_user_value}")


        
    

def computer_card_one():
    computer_cards = random.choice(all_numbers)
    print(f"Computer first card is {computer_cards}")
    return computer_cards







def computer_card_deal(computer_one):
    computer_cards = []
    computer_cards.append(computer_one)
    # print(f"Computer card is {computer_cards}")
    computer_total = computer_cards[0]
    
    while computer_total<16:
        t = random.choice(all_numbers)
        if t == 11:
            t = check_ace(computer_total + t)
        computer_cards.append(t)
        computer_total += t
    print(f"Computer card is {computer_cards} and the final score is {computer_total}")
    return computer_total




def main():
   
 
    computer_one = computer_card_one()
    user_total = dealing_user_card()
    if user_total > 21 :
        print(f"You went over. You lose 😭")
    elif user_total == 21:
        print(f"Your total: {user_total} == 21, YOU WON")        

    else:
        computer_total = computer_card_deal(computer_one)

        
        if user_total > computer_total or computer_total> 21:
            print("You won")
        elif user_total == computer_total:
            print("Its a draw")
        else:
            print("Computer win")
    choice = True
    while choice:
        choice= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if choice == 'y':
            print('''       \n ''')
            main()
        else:
            choice = False





main()






