import random
#Gives instructions
def print_message():
  print("Welcome to the Rock,Paper and Scissors!")
  print("Instructions:-")
  print("1] Enter valid inputs like rock,paper and scissors.")
  print("2]rock beats scissors,scissors beat paper, and paper beats rock.")
  print("3]Choose your input and computer will choose his input.")
  print("4]Both the inputs will be compared and result will be declared.")
  print("! ENJOY PLAYING !")
  print("Let,s start the game")

#For computers random choice
def get_computer_choice():             
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
#For finding the winner
def determine_winner(user_choice, computer_choice):       
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
#For playing games
def play_game():
  print_message()            
  while True:
        # Get the user's choice
        user_choice = input("Enter your choice (rock, paper, or scissors):- ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue
        computer_choice = get_computer_choice()
        # Display both choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        # Determine and display the winner
        result = determine_winner(user_choice, computer_choice)
        print(result) 
        a = input("Do you want to play again? (yes/no):-")
        if a.lower() == 'yes':
            continue
        else:
            break    
# Start the game
play_game()
