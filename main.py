import random
import time
import sys

def loading():
  for i in range(4):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.5)
  print()

def pr():
  for i in range(10):
    sys.stdout.write("oh")
    sys.stdout.flush()
    time.sleep(0.2)
  print() 

def number_guessing_game():
  print("Choose Tum konsi level khelna chahate ho: \n1. Level Easy: 10 attempt\n2. Level Medium: 7 attempt\n3. Level Hard :5 attempt")
  while True:
    ch=(int(input("\n1.,2.,3...?:")))
    if ch==1:
      attempt_left=10
      a=10
      break
    elif ch==2:
      attempt_left=7
      a=7
      break
    elif ch==3:
      attempt_left=5
      a=5
      break
    else:
      print("\noption diya hai usme se select kro....")
  select=random.randint(1,100)
  print("Ruko jara Sabar karo, Secret Number Sochne Do")
  loading()
  print("Soch liya..")

  while attempt_left>0:
    try:
      guess=int(input("\nGuess Batao 1 to 100 :"))
      if guess==select:
        if attempt_left in (10,7,5):
          pr()
          print("7 cr....")
          time.sleep(1)
          print("\nSahi javab in 1st try. Attempt remaining = ",attempt_left," Secret Number = ",select)
        else:
          print("\nCongrats.. Sahi guess. Attempt remaining = ",attempt_left," Secret Number = ",select)
        break
      elif guess < select:
        remain=attempt_left-1
        print("\nBahut chota number Guess kiya. Attempt remaining = ",remain)
        while True:
          if a==10:
            if (select-guess)<=5:
              print("Hint: Tumhara guess 5 ke range me hai.")
              break
            elif (select-guess)<=20:
              print("Hint: Tumhara guess 20 ke range me hai.")
              break
            else:
              break
          elif a==7:
            if (select-guess)<=5:
              print("Hint: tumhara guess bahut karib hai")
              break
            else:
              break
          elif a==5:
            if attempt_left<=3:
              while True:
                b=input("\nHint chahiye..?(ha/na)")
                if b=="ha":
                  if select<50:
                    print("Hint: Number 51 se chota hai..")
                    break
                  else:
                    print("Hint: Number 50 se bada Hai..")
                    break
                elif b=="na":
                  print("okk,Agee badte hai.")
                  break
                else:
                  print("ha ya na..?")
              break
            else:
              break
          else:
            break
      else:
        remain=attempt_left-1
        print("\nBahut Bada nnmber Guess Kiya. Attempt remaining = ",remain)
        while True:
          if a==10:
            if (guess-select)<=5:
              print("Hint: Tumhara guess 5 ke range me hai.")
              break
            elif (guess-select)<=20:
              print("Hint: Tumhara guess 20 ke range me hai.")
              break
            else:
              break
          elif a==7:
            if (guess-select)<=5:
              print("Hint: tumhara guess bahut karib hai")
              break
            else:
              break
          elif a==5 :
            if attempt_left<=4:
              while True:
                b=input("\nHint chahiye..?(ha/na)")
                if b=="ha":
                  if select<50:
                    print("Hint: Number 51 se chota hai..")
                    break
                  else:
                    print("Hint: Number 50 se bada Hai..")
                    break
                elif b=="na":
                  print("okk,Agee badte hai.")
                  break
                else:
                  print("ha ya na..?")
              break
            else:
              break
          else:
            break
      attempt_left -= 1
    except ValueError:
      print("1 to 100 ke bich mese batao..!")
  
  if attempt_left==0:
    print("\nOps.. Sab attempt khatam Hogaye. Attempt remaining = ",attempt_left," Secret Number was = ",select)
  time.sleep(2)
number_guessing_game()