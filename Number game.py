import random
print(" I will generate number between 1 to 10 and you have to guess it ")

guess = int(input(" Enter your guess: "))

number= (random.randint(1,5))

if number == guess:
    print(" Congratulations! You guessed it right.")
    print(" The number was:", number)
else:
    print(" Sorry, you guessed it wrong.")
    print(" The number was:", number)

print(" Thank you for playing the game!")
print("Let's play rock, paper, scissors game now!")

computer= random.choice(['rock', 'paper', 'scissors'])
user = input(" Enter your choice (rock, paper, scissors): ").lower()
if user == computer:
    print(" It's a tie! Both chose", user)
elif computer == 'rock 'and user == 'scissors' or computer == 'scissors' and user == 'paper' or computer == 'paper' and user == 'rock':
    print(" You lose! Computer chose", computer and " you chose", user)

else:
    print(" You win! Computer chose", computer)
    



