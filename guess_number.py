def guess_number():
    n = 90
    n_guess = 5
    # number_of_guesses = 10
    # number_of_guesses = guess_number - 1


    print("Guess the number and the number is between 1 - 100.")
    print("You have only 5 no. of guessing.")

    while n_guess != 0:
        user  = int(input("Guess the number:"))
        # print(n_guess," no. of guesses left.\n")
        n_guess = n_guess - 1
        print(n_guess," no. of guesses left.\n")

        if user > n:
            print("Think little smaller.\n")
        elif user < n:
            print("Think little larger.\n")
        elif user == n:
            print("Congrats! you won.")
            break
        if n_guess == 0:
            print("Game Over")
            
    
            

guess_number()



