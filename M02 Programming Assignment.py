# 4.1

secret = 5
guess = int(input("Please input a number 1-10: "))

if guess == secret:
    print("Just Right")
elif guess > secret:
    print("Too High")
else:
    print("Too Low")

# 4.2

while True:
    quest1 = input ("Is your food small? ")
    if quest1 == 'Yes':
        small = True
        break
    else:
        small = False
        break

while True:
    quest2 = input("Is your food green? ")
    if quest2 == 'Yes':
        green = True
        break
    else:
        green = False
        break

if small and green:
    print("Pea")
elif small and not green:
    print("Cherry")
elif not small and green:
    print("Watermelon")
else:
    print("Pumpkin")

# 6.1

list = [3, 2, 1, 0]

for value in list:
    print(value)

# 6.2

guess_me = 7
number = 1

while number <= guess_me:
    if number < guess_me:
        print("Too Low")
    elif number == guess_me:
        print("Found It!")
        break
    else:
        print ("Oops")
        break
    number += 1
              
# 6.3

guess_me = 5

for number in range(10):
    if number < guess_me:
        print("Too Low")
    elif number == guess_me:
        print("Found It!")
        break
    else:
        print ("Oops")
        break










