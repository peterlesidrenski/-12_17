name = input()
password=4123
print(password)
guess = int(input())
while password != guess:
        print("try again")
        guess = int(input())
        if guess == password:
            print("wellcome")