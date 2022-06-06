#chances = 'guesses'
from random import randint
import turtle

num = randint(1,3)

chances = 6
correct = 0

showGuess = ['_','_','_']
wordList = ['dog','cat','rat','pig']

window=turtle.Screen()
window.bgcolor('black')
j=turtle.Turtle()
j.shape('turtle')
j.speed(10)
j.pencolor ('white')

print(" ".join(showGuess))
word = wordList[num]
while chances > 0 and correct < 3:
    guess = input ('Guess a letter.')
    if guess == word[0] or guess == word[1] or guess == word[2]:
        print ('You correctly guessed the letter',guess,'!')
        correct += 1
        print ('You have',chances,'guesses left.')
        for i in range(3):
            if word[i] == guess:
                showGuess[i] = guess
                print(" ".join(showGuess))
        if correct == 3:
            print ('You got the word! Amazing job!')
            print ('The word was ',wordList[num],'.')
    else:
        print ('Oh no! You guessed wrong!')
        chances -= 1
        print ('You have',chances,'guesses left.')
        match (chances){
            case 0:
                j.backward(100)
                j.left(90)
                j.forward(100)
                print ('Your man got hung :(. The correct word was.', wordList[num])
            case 1:
                j.backward(100)
                j.right(55)
                j.forward(200)
                j.right(45)
                j.forward(100)
                
            case 2:
                j.backward(100)
                j.left(110)
                j.forward(100)
            case 3:
                j.backward(200)
                j.right(55)
                j.forward(100)
            case 4:
                j.right(90)
                j.forward(250)
            case 5:
                j.circle(50)
        }
