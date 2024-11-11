import numpy as np
import os
import time
import threading

os.system("cls")

player1 = input("\n\nOnnam kalikkarante peru : ").upper()
player2 =  input("\n\nRandaam kalikkarante peru : ").upper()

global rounds
rounds = int(input("\n\nEthra round kalikkanam : "))
rounds*=2
player1_score = 0
player2_score = 0
tie_breaker_random=0
word_set_time = 60
letter_guess_time = 30
word = ""

def initiate_hangman():
    global rounds
    global player1_score
    global player2_score
    global word_set_time;letter_guess_time

    if tie_breaker_random == 0:
        if rounds%2==0:
            setter=player1
            finder=player2
        else:
            setter=player2
            finder=player1
    
    elif tie_breaker_random == 1:
        setter=player1
        finder=player2 
        print(f"\n\n{setter} IS THE SETTER AND {finder} IS THE FINDER.")
    
    elif tie_breaker_random == 2:
        setter=player2
        finder=player1
        print(f"\n\n{setter} IS THE SETTER AND {finder} IS THE FINDER.")

    word = str(input(f"\n\n{setter} : Enter the word you want {finder} to guess ...\nYou have 1 minute...\n"))
    word = word.upper()
    n = len(word)

    os.system('cls')

    spaces = np.repeat("_",n)
    letters = np.empty(n,dtype=str)
    tries=0

    hangman = np.array(["H","A","N","G","M","A","N"])

    for x in range(n):
        letters[x] = word[x] 

    while tries<7:
        for x in spaces:
            print(x,end =" ")

        print("\t\t\t\t\t\t\t\t\t\t",end=" ")

        for x in range(tries):
            print(hangman[x],end=" ")
        
        print(f"\n\n\t\t\t\t\t\t\t\t\t{player1} - {player1_score}\t\t\t{player2} - {player2_score}")

        ans = input(f"\n\n\n{finder} : Guess a letter in the word : ")
        ans = str(ans.upper())

        i=0
        j=0

        for x in letters:
            if x==ans:
                index = np.argwhere(letters==ans)
                for w in index:
                    spaces[w]=ans
                i+=1

        if i==0: 
            tries+=1
    
        print("\n")
    
        for x in range(n):
            if letters[x]==spaces[x]:
                j+=1

        if j==n:
            break
    
    if tie_breaker_random == 0:
        if j==n:
            print("\n\nNEE ORU KILLEDI THANNE.....")
            print(f"\n\n{finder} WINS THE ROUND.")
            if rounds%2==0:
                player2_score+=1
            else:
                player1_score+=1
            print(f"\n\n{player1} - {player1_score}\t\t\t{player2} - {player2_score}")
        else:
            if rounds%2==0:
                player1_score+=1
            else:
                player2_score+=1
            print("\t\t\t\t\t\t H  A  N  G  M  A  N")
            print("\n\nGAME OVER NIGGA....")
            print(f"\n\nThe word was {word}")
            print(f"\n\n{setter} WINS THE ROUND")
            print(f"\n\n{player1} - {player1_score}\t\t\t{player2} - {player2_score}")
    
    elif tie_breaker_random == 1:
        if j == n:
            print("\n\nNEE ORU KILLEDI THANNE.....")
            print(f"\n\n{finder} WINS THE GAME ... HEHE")
        else:
            print("\t\t\t\t\t\t H  A  N  G  M  A  N")
            print("\n\nGAME OVER NIGGA....")
            print(f"\n\nThe word was {word}")
            print(f"\n\n{setter} WINS THE GAME ... HEHE ")
    
    elif tie_breaker_random == 2:
        if j == n:
            print("\n\nNEE ORU KILLEDI THANNE.....")
            print(f"\n\n{finder} WINS THE GAME ... HEHE")
        else:
            print("\t\t\t\t\t\t H  A  N  G  M  A  N")
            print("\n\nGAME OVER NIGGA....")
            print(f"\n\nThe word was {word}")
            print(f"\n\n{setter} WINS THE GAME ... HEHE ")
    
    rounds-=1
    print()
    print()
    print()

'''def word_set_timer():
    global word 
    global word_set_times
    while word_set_time>=0:
        time.sleep(1)
        word_set_time-=1
        if word_set_time!=0:
            if len(word):
                break
            if word_set_time == 30:
                print(f"You have {word_set_time} more seconds...")
            elif word_set_time == 10:
                print(f"You have {word_set_time} more seconds...")
            elif word_set_time == 5:
                print(f"You have {word_set_time} more seconds...")
'''
while rounds > 0 : 
    initiate_hangman()

if player1_score > player2_score:
    print(f"\n\n\t\t\t\t\t\t {player1} IS THE WINNER HEHE . . .")

elif player2_score > player1_score:
    print(f"\n\n\t\t\t\t\t\t {player2} IS THE WINNER HEHE . . .")

else:
    print(f"\n\n\t\t\t\t\t\t\tIT'S A TIE ....")
    rounds = int(input("\n\n\t\t\t\t\tEnter 1 for tie breaker round or enter 0 to stop the game : "))
    if rounds == 1:
        print(f"\n\nA SINGLE ROUND TO BREAK THE TIE")
        print(f"COMPUTER WILL SELECT A PLAYER TO SET THE WORD AND THE OTHER SHOULD GUESS THE WORD (THE SELECTION IS TRULY RANDOM)")
        tie_breaker_random = np.random.choice([1,2])
        rounds/=2
        initiate_hangman()

print()
print()
print()
print()
print()
print()
print()
print()
print() 
print()