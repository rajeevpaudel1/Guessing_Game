secret_number = 5
guess_count = 0
guess_limit = 3
print("You will be provided with the 3 chances to guess the number")
while guess_count < guess_limit:
    guess = int(input("Enter the number: "))
    guess_count += 1
    if guess == secret_number:
        print("You are right! ")
        break
else:
    print("You failed! ")



