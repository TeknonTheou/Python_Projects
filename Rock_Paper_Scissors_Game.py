def start():
    print('This is my Rock, Paper, Scissors Game!')
    Player_One=input('Please provide name of player 1: ')
    Player_Two=input('Please provide name of player 2: ')
    def choices(Player_One_Choice, Player_Two_Choice):
        if Player_One_Choice=='rock' and Player_Two_Choice=='paper':
            return('Paper covers Rock! ' + Player_Two + ' wins!')
        elif Player_One_Choice=='paper' and Player_Two_Choice=='rock':
            return ('Paper covers Rock! ' + Player_One + ' wins!')
        elif Player_One_Choice=='scissors' and Player_Two_Choice=='paper':
            return ('Scissors cuts Paper! ' + Player_One + ' wins!')
        elif Player_One_Choice=='rock' and Player_Two_Choice=='scissors':
            return ('Rock smashes Scissors! ' + Player_One + ' wins!')
        elif Player_One_Choice=='paper' and Player_Two_Choice=='scissors':
            return ('Scissors cuts Paper! ' + Player_Two + ' wins!')
        elif Player_One_Choice=='scissors' and Player_Two_Choice=='rock':
            return ('Rock smashes Scissors! ' + Player_Two + ' wins!')
        elif Player_One_Choice==Player_Two_Choice:
            return(Player_One + ' and ' + Player_Two + ' tied!')
        else:
            return('Please type Rock, Paper, or Scissors.')
    Player_One_Choice = input('Does ' + Player_One + ' choose Rock, Paper, or Scissors?').lower()
    Player_Two_Choice = input('Does ' + Player_Two + ' choose Rock, Paper, or Scissors?').lower()
    print(choices(Player_One_Choice, Player_Two_Choice))

    def Play_Again():
        Again=input('Would you like to play the game again?').lower()
        if Again=='No'.lower():
            quit()
        if Again=='Yes'.lower():
            start()
        else:
            print('Please enter Yes or No. Thank you!')
            Play_Again()
    Play_Again()
start()
