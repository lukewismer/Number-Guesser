import random
import os
import time
from datetime import date
from datetime import datetime
import sys
import pandas as pd
from operator import itemgetter
os.system('clear')
ur_name = input('What is your Name: ')
os.system('clear')
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
def Menu():
    today_set = date.today()
    today = today_set.strftime("%B %d, %Y")
    now = datetime.now()
    time_now = now.strftime("%H: %M: %S")
    print(color.PURPLE + '-------------------------------------------' + color.END)
    print(color.BLUE + 'Welcome to number guesser ' + ur_name + color.END)
    print(color.PURPLE + '-------------------------------------------' + color.END)
    time.sleep(2.5)
    os.system('clear')
    print(color.GREEN + 'Date: ' + str(today) + color.END)
    print(color.GREEN + 'Time: ' + str(time_now) + color.END)
    time.sleep(1.5)
    print(color.BOLD + color.RED + color.UNDERLINE + 'MENU' + color.END)
    print('  - Press a to play')
    print('  - Press x to quit')
    print('  - Press l to view leaderboard')
    #print('  - Press s to go to settings')
    command = input()
    os.system('clear')
    return command
def quit():
    sys.exit()
def Play(n):
    guess_num = 0
    done = False
    answer = random.randint(0, n)
    poss = []
    difficulty_level = n/10
    while not done:
        os.system('clear')
        print(color.RED + "You have guessed " + str(guess_num) +' times' + color.END)
        print(color.GREEN + "You have already guessed : " + str(poss) + color.END)
        guess = input("Guess a number between 1 and " + str(n) + ': ')
        guess = int(guess)
        if guess == answer:
            guess_num += 1
            print("Correct!")
            score = (difficulty_level+(difficulty_level/2)/guess_num)
            f = open("leaders.text", "a")
            print(str(guess_num),str(score), ur_name, str(difficulty_level), file=open("leaders.txt", "a"))
            print(ur_name + ' took ' + str(guess_num) + ' guesses on difficulty level ' + str(difficulty_level))
            print("Your final score is: " + str(score))
            f.close()
            done = True
        if guess != answer:
            guess_num += 1
            poss.append(guess)
            if guess > answer:
                print("Your guess was too high!")
                time.sleep(2)
            if guess < answer:
                print("Your guess was too low!")
                time.sleep(2)
            if guess > n or guess < 0:
                print("Your guess was out of range, the range is: 1,"+str(n))
                time.sleep(2)
def Leaderboard():
    with open("leaders.txt") as inf:
        data=[]
        for line in inf:
            line = line.split()
            if len(line)==4:
                data.append(tuple(line))
    data = sorted(data, key=itemgetter(0), reverse=True)
    df = pd.DataFrame(data)
    df.columns = ['Guesses', 'Score', 'Name', 'Difficulty']
    print(df)
    time.sleep(4)
    quit_l = input('Press x if you would like to quit: ')
    if quit_l == 'x':
        sys.exit()
def Run():
    Menu()

    command = Menu()
    if command == 'l':
        Leaderboard()
    if command == 'x':
        sys.exit(color.RED + ur_name + ' exited the game' + color.END)
    if command == 'a':

        os.system('clear')
        print(color.BOLD + color.UNDERLINE + 'Select a Difficulty' + color.END)
        print(color.GREEN + '1' + color.END)
        print(color.YELLOW + '2' + color.END)
        print(color.CYAN + '3' + color.END)
        print(color.DARKCYAN + '4' + color.END)
        print(color.BLUE + '5' + color.END)
        print(color.PURPLE + '6' + color.END)
        print(color.RED + '7' + color.END)
    level = input()
    level = int(level) * 10
    Play(level)
Run()