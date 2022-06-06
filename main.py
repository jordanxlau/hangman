#chances = 'guesses'
import random
word=random.randint(1,3)

chances = 6
correct = 0

import turtle
window=turtle.Screen()
window.bgcolor('black')
j=turtle.Turtle()
j.shape('turtle')
j.speed(10)
j.pencolor ('white')

if word == 1:
    li_st=['_','_','_']
    print(" ".join(li_st))
    word1 = 'cat'
    while chances > 0 and correct < 3:
        guess=input ('Guess a letter.')
        if guess == word1[0] or guess == word1[1] or guess == word1[2]:
            print ('You correctly guessed the letter',guess,'!')
            correct = correct + 1
            print ('You have',chances,'guesses left.')
            for i in range(3):
                if word1[i] == guess:
                    li_st[i] = guess
                    print(" ".join(li_st))
            if correct == 3:
                print ('You got the word! Amazing job!')
                print ('The word was CAT.')
        else:
            print ('Oh no! You guessed wrong!')
            chances = chances - 1
            print ('You have',chances,'guesses left.')
            if chances == 0:
                j.backward(100)
                j.left(90)
                j.forward(100)
                print ('Your man got hung :P. The correct word was CAT.')
            elif chances == 1:
                j.backward(100)
                j.right(55)
                j.forward(200)
                j.right(45)
                j.forward(100)
            elif chances == 2:
                j.backward(100)
                j.left(110)
                j.forward(100)
            elif chances == 3:
                j.backward(200)
                j.right(55)
                j.forward(100)
            elif chances == 4:
                j.right(90)
                j.forward(250)
            elif chances == 5:
                j.circle(50)

if word == 2:
    li_st=['_','_','_','_']
    print(" ".join(li_st))
    word1 = 'fish'
    while chances > 0 and correct < 4:
        guess=input ('Guess a letter.')
        if guess == word1[0] or guess == word1[1] or guess == word1[2] or guess == word1[3]:
            print ('You correctly guessed the letter',guess,'!')
            correct = correct + 1
            print ('You have',chances,'guesses left.')
            for i in range(4):
                if word1[i] == guess:
                    li_st[i] = guess
                    print(" ".join(li_st))
            if correct == 4:
                print ('You got the word! Amazing job!')
                print ('The word was FISH.')
        else:
            print ('Oh no! You guessed wrong!')
            chances = chances - 1
            print ('You have',chances,'guesses left.')
            if chances == 0:
                j.backward(100)
                j.left(90)
                j.forward(100)
                print ('Your man got hung :P. The correct word was FISH.')
            elif chances == 1:
                j.backward(100)
                j.right(55)
                j.forward(200)
                j.right(45)
                j.forward(100)
            elif chances == 2:
                j.backward(100)
                j.left(110)
                j.forward(100)
            elif chances == 3:
                j.backward(200)
                j.right(55)
                j.forward(100)
            elif chances == 4:
                j.right(90)
                j.forward(250)
            elif chances == 5:
                j.circle(50)

if word == 3:
    li_st=['_','_','_']
    print(" ".join(li_st))
    word1 = 'dog'
    while chances > 0 and correct < 3:
        guess=input ('Guess a letter.')
        if guess == word1[0] or guess == word1[1] or guess == word1[2]:
            print ('You correctly guessed the letter',guess,'!')
            correct = correct + 1
            print ('You have',chances,'guesses left.')
            for i in range(3):
                if word1[i] == guess:
                    li_st[i] = guess
                    print(" ".join(li_st))
            if correct == 3:
                print ('You got the word! Amazing job!')
                print ('The word was DOG.')
        else:
            print ('Oh no! You guessed wrong!')
            chances = chances - 1
            print ('You have',chances,'guesses left.')
            if chances == 0:
                j.backward(100)
                j.left(90)
                j.forward(100)
                print ('Your man got hung :P. The correct word was DOG.')
            elif chances == 1:
                j.backward(100)
                j.right(55)
                j.forward(200)
                j.right(45)
                j.forward(100)
            elif chances == 2:
                j.backward(100)
                j.left(110)
                j.forward(100)
            elif chances == 3:
                j.backward(200)
                j.right(55)
                j.forward(100)
            elif chances == 4:
                j.right(90)
                j.forward(250)
            elif chances == 5:
                j.circle(50)




        
