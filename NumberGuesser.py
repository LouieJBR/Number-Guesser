import random #import random module for generation of random integers

target = (random.randint(0,20)) #generate a random number within a range, will be the target
score = 0 #users score, each guess will add one to this score

while True: 
    guess = input("Please enter your guess ") #the user will input their guess
    converted_guess = int(guess) #the users input will be converted to an integer for comparison
    score = score + 1 #score is incremented by one

    if converted_guess > target: #if the users guess is higher than the target
        print("Target is lower!")
    elif converted_guess < target:#if the users guess is lower than the target
        print("Target is higher!")
    else: #if the users input is neither higher or lower, correct
        break #break the while loop

print("Congratulations! Your guess was correct!") #congratulate user for guessing correctly

final_score = 101-score #calculate final score, the total value will be subtracted from 101 for final high score, 101 so that first time guess will produce a score of 100

print("Your final score was " + str(final_score)) #print the users final score
