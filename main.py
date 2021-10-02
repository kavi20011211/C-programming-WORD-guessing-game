import random

with open('CODE(2)','r') as f:
    blocks= f.readlines()

blocks= random.choice(blocks)[:-1]

allow_errors= 7
guesses=[]
done=False

while not done:
    for letter in blocks:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_",end=" ")
    print("")



    guess=input(f" Allowed errors left {allow_errors}, Next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in blocks.lower():
        allow_errors -=1
        if allow_errors==0:
            break

    done=True
    for letter in blocks:
        if letter.lower() not in guesses:
            done=False

if done:
    print(f" You have found the word {blocks}!")

else:
    print(f" Game is over! the word was {blocks}!")

