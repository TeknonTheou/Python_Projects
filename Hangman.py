import random
import turtle
turtle.pensize(5)


Words=['Apple', 'Butterfly','Chocolate','Dinosaur', 'Elephant', 'Firetruck','Genius','Hospital', 'Island', 'Jackrabbit', 'Kangaroo', 'Leopard', 'Marshmallow', 'Necklace', 'Ostrich']
print('This game was created by Billy McMillen.')
print('Welcome to my guessing game!')
print('In this program, you will try to guess a word that I chose.')
print('Good luck!')

def start():
    Player_Name = input('What is the name of the player? ')
    print('Greeting, ' + Player_Name + '! It is time to guess!')
    Selection=random.choice(Words)
    Secret_Word=Selection.lower()
    Guesses = ' '
    Turns_Left=10

    import turtle
    turtle.pensize(5)
    errors = 0

    def showStickman():
        if(errors==1):
            turtle.bk(100)
            turtle.fd(200)
        if(errors==2):
            turtle.bk(100)
            turtle.lt(90)
            turtle.fd(300)
        if(errors==3):
            turtle.rt(90)
            turtle.fd(150)
        if(errors==4):
            turtle.rt(90)
            turtle.fd(50)
        if(errors==5):
            turtle.dot(50)
        if(errors==6):
            turtle.fd(100)
            turtle.bk(75)
        if(errors==7):
            turtle.rt(45)
            turtle.fd(50)
            turtle.bk(50)
        if(errors==8):
            turtle.lt(90)
            turtle.fd(50)
            turtle.bk(50)
        if(errors==9):
            turtle.rt(45)
            turtle.fd(75)
            turtle.rt(45)
            turtle.fd(50)
            turtle.bk(50)
        if(errors==10):
            turtle.lt(90)
            turtle.fd(50)

    while Turns_Left>0:
        Wrong_Answers = 0
        for Letter in Secret_Word:
            if Letter in Guesses:
                print(Letter)
            else:
                print('_')
                Wrong_Answers += 1
        if Wrong_Answers==0:
            print('YOU WIN! You guessed my word: ' + Secret_Word + '!!!!!')
            Play_Again()
        Guess = input('Guess a letter here: ').lower()
        Guesses += Guess

        if Guess not in Secret_Word:
            Turns_Left -= 1
            errors=errors+1
            showStickman()
            print('Oops! This letter is not in my word.  Please try again.')
            print('You have ' + str(Turns_Left) + ' more guesses left. You can do it!')
            if Turns_Left==0:
                print('GAME OVER')
                Play_Again()




def Play_Again():
    Again=input('Would you like to play again? ').lower()
    if Again=='No'.lower():
        quit()
    if Again=='Yes'.lower():
        turtle.reset()
        start()
    else:
        print('Please enter Yes or No. Thank you!')
        Play_Again()

start()
