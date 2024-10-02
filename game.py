import random
name=input("ENTER YOUR NAME :- ")
print('______________________________________________________________________')
print("WELCOME ",name.upper()," TO THE GAME OF ROCK PAPER SCISSORS" )
print('----------------------------------------------------------------------')
print("""
PRESS 1 FOR ROCK
PRESS 2 FOR PAPER
PRESS 3 FOR SCISSORS
PRESS -1 TO STOP THE GAME
MAX NUMBER OF ATTEMP IS 25
IF THE SCORE OF ANY REACH 5 THE GAME IS OVER    """)
print("----------------------------------------------------------------------")

user_score=0
com_score=0
attempt=0

symbol={1:'ROCK', 2:'PAPER', 3:'SCISSORS'}

def draw():#function for draw   #code for draw the point
 print(name.upper(),":-",symbol[user_input])
 print("COMPUTER",":-",symbol[com_input])
 print("DRAW THE POINT")
 print("COMPUTER SCORE :-",com_score)
 print(name.upper(),"SCORE :-",user_score)
 print("ATTEMPT :-",attempt)
 print("----------------------------------------------------------------------")

def compoint():#function for computer point  #code for computer got apoint
  print(name.upper(),":-",symbol[user_input])
  print("COMPUTER",":-",symbol[com_input])
  print("COMPURT GOT A POINT")
  print("COMPUTER SCORE :-",com_score)
  print(name.upper(),"SCORE :-",user_score)
  print("ATTEMPT :-",attempt)
  print("----------------------------------------------------------------------")

def userpoint():#function for computer point  #code for user got a point
  print(name.upper(),":-",symbol[user_input])
  print("COMPUTER",":-",symbol[com_input])
  print(name.upper()," GOT A POINT")
  print("COMPUTER SCORE :-",com_score)
  print(name.upper(),"SCORE :-",user_score)
  print("ATTEMPT :-",attempt)
  print("----------------------------------------------------------------------")

def userwon():  #code for user won
    print("CONGRATULATIONS ",name.upper()," IS THE WINNER")
    print("SCORE OF ",name.upper()," IS :-",user_score)
    print("ATTEMPT :-",attempt)
    print("PRESS RUN BUTTON TO PLAY THE GAME AGAIN")
    print("--------------------------------------------------------------------")

def comwon():  #code for computer won
    print("COMPUTER WON THE GAME")
    print("SCORE OF COMPUTER IS :-",com_score)
    print("ATTEMPT :-",attempt)
    print("PRESS RUN BUTTON TO PLAY THE GAME AGAIN")
    print("--------------------------------------------------------------------")

def drawma():  #code for draw the match
    print("DRAW THE MATCH")
    print("SCORE OF ",name.upper()," IS :-",user_score)
    print("SCORE OF COMPUTER IS :-",com_score)
    print("ATTEMPT :-",attempt)
    print("PRESS RUN BUTTON TO PLAY THE GAME AGAIN")
    print("--------------------------------------------------------------------")

for i in range(25) :
 if user_score==5:
     break;
 elif com_score==5:
     break;
 elif attempt==25:
    break;
 com_input=random.randint(1,3)
 user_input=int(input("ENTER YOUR OPTION :- "))

 if user_input==1 and com_input==1:
     attempt+=1
     draw()

 elif user_input==2 and com_input==2:
     attempt+=1
     draw()

 elif user_input==3 and com_input==3:
     attempt+=1
     draw()

 elif user_input==1 and com_input==2:
     com_score+=1
     attempt+=1
     compoint()

 elif user_input==2 and com_input==1:
     user_score+=1
     attempt+=1
     userpoint()

 elif user_input==2 and com_input==3:
     com_score+=1
     attempt+=1
     compoint()

 elif user_input==3 and com_input==2:
     user_score+=1
     attempt+=1
     userpoint()

 elif user_input==1 and com_input==3:
     user_score+=1
     attempt+=1
     userpoint()

 elif user_input==3 and com_input==1:
     com_score+=1
     attempt+=1
     compoint()

 elif user_input==-1:
    break;
    print("----------------------------------------------------------------------")

 else:
     print("INVALID NUMBER FOR THE GAME")
     attempt+=1
     print("ATTEMPT:- ",attempt)
     print("----------------------------------------------------------------------")

print("----------------------------------------------------------------------")

if user_score==5 or com_score==5 and user_input!=-1 : #first rule
 print("THE GAME IS OVER")
 if user_score>com_score:
    userwon()
 elif com_score>user_score:
     comwon()

elif attempt==25:  #second rule
 print("YOU REACHED THE MAXIMUM ATTEMPT")
 if user_score>com_score:
   userwon()
 elif com_score>user_score:
   comwon()
 else:
    drawma()

else:  #third rule
 print("MATHCH STOPED IN HALF THE WAY BECAUCE YOU PRESSED -1")
 if user_score>com_score:
    userwon()
 elif com_score>user_score:
     comwon()
 else:
    drawma()

