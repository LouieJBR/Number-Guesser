import random #import random module for generation of random integers

print("Welcome to Number Guesser!") #greet user
print("Before we begin, please declare a range for the random number...") #make them aware of what they have to first do

user_declared_lowerrange = input("Lowest range value ") #allow the user to set the lowest value
user_declared_upperrange = input("Highest range value ") #allow the user to set the highest value
print("")
print("How many guesses is the user allowed ?")
user_declared_guessamount = input("Number of guesses allowed ") #allow the user to decide how manu guesses the user gets
print("")

input("Press Enter to begin guessing...") #when ready, user must press enter to begin

lower_range = int(user_declared_lowerrange) #convert the users input to an integer (low range)
upper_range = int(user_declared_upperrange) #convert the users input to an integer (high range)
guesses_allowed = int(user_declared_guessamount) #convert the users input to an integer (number of guesses)

target = (random.randint(lower_range, upper_range)) #generate a random number within a range, will be the target
score = 0 #users score, each guess will add one to this score
print("")

while True: 
    guess = input("Please enter your guess ") #the user will input their guess
    converted_guess = int(guess) #the users input will be converted to an integer for comparison
    score = score + 1 #score is incremented by one

    if score == guesses_allowed: #checks if the users score (number of attempts) is the same as the number of guesses allowed, ran out
        print("You have ran out of guesses...")
        break #break loop
    else:
        if converted_guess > target: #if the users guess is higher than the target
            print("Target is lower!")
        elif converted_guess < target:#if the users guess is lower than the target
            print("Target is higher!")
        else: #if the users input is neither higher or lower, correct
            print("Congratulations! Your guess was correct!") #congratulate user for guessing correctly
            final_score = 100 - ((score/guesses_allowed)*100) #final score will be the users attempts, divided by number allowed, multiplied by 100 then subtracted from 100
            print("Your final score was " + str(final_score)) #print the users final score

            break #break the while loop
