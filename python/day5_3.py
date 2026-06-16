num=int(input("Guess the secret number between 1 to 10: "))
secret_num=7
while num!=secret_num:
    print("Wrong!! try again")
    num=int(input("Guess the secret number between 1 to 10: "))
print("Congratulations!!")