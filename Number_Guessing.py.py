import random
n=random.randint(1, 50)
a=-1
guesses= 1
while (a != 0):
    a = int(input('Guess the number:'))
    if (a >n):
        print('Lower number please')

        guesses+=1
    elif (a<n):
        print('Higher number please')
        guesses+=1
    else:
        break
print(f"You have guessed the correctly number {n} in {guesses} attempts ")
