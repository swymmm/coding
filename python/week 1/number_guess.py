secret_num=55
attempt=0
max_attempts=10
guessed=False

print("-----------------Number guessing game----------------")
print(f"Guess the number between 1- 100.You have {max_attempts} attempts left.")

while attempt<max_attempts:
    guess=int(input(f"Attempt: {attempt+1} Take a guess: "))
    attempt +=1
    if guess==secret_num:
        print(f"Congratulations!! you guessed it in {attempt} attempts.")
        guessed=True
    elif guess<secret_num:
        remaining=max_attempts-attempt
        print(f"Too low!!.You have {remaining} attempts left.")
    else:
        remaining=max_attempts-attempt
        print(f"Too high!!.You have {remaining} attempts left.")
if not guessed:
    print(f"Game over!!.The secret number was {secret_num}.")
print("Thank you for playing!")