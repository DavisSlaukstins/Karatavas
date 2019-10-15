import random
import time

#main koda sakums
def get_guess():

  #gretings sequence
  print("Welcome")
  name = str(input("Wats your name? :"))
  print("Hey ",name,"good luck!")
  time.sleep(2)
  print("let's begun")
  print("Making up a word....")
  time.sleep(3)

#sak laiku
  print("Starting time")
  start_time = time.time()

#limenu sakums
  lvl = 1

  #ieliek visas word bankas, kas ir apaksa, un vares sakt vinas lietot
  global secret_word1
  global secret_word2
  global secret_word3
  global secret_word4
  global secret_word5

#kamer limenis nebus lielaks par pieci spele turpinasies
  while lvl < 6:
    #atkariba no limena, izmanto vardus no ta limena paredzetas vardu bankas
    if lvl == 1:
      secret_word = secret_word1
    if lvl == 2:
      secret_word = secret_word2
    if lvl == 3:
      secret_word = secret_word3
    if lvl == 4:
      secret_word = secret_word4
    if lvl == 5:
      secret_word = secret_word5
#parada kura limeni tu atrodies
    if lvl > 0:
      print("")
      print("level",lvl)
      
#saprot cik daudz jabut dashiem atkariba no varda garuma
      dashes = "-" * len(secret_word)

      #vins norada cik ir dzivibas atkariba no limena
      if lvl == 1:
        guesses_left = 4
      if lvl == 2:
        guesses_left = guesses_left+1
      if lvl == 3:
        guesses_left = guesses_left+1
      if lvl == 4:
        guesses_left = guesses_left+1
      if lvl == 5:
        guesses_left = guesses_left+1

#kamer dzivibas ir vairak par nuli un vards nav uzminets tikmer spele turpinas
      while guesses_left > 0 and not dashes == secret_word:

#atkariba no ta cik tev ir dzivibas vins printe karatavu caliti
        if guesses_left >= 4:
            print("""      ____
     |    |
     |    
     |
     |
     |
     |
    [_]""")
        if guesses_left == 3:
            print("""      ____
     |    |
     |    0
     |
     |
     |
     |
    [_]""")
        if guesses_left == 2:
            print("""      ____
     |    |
     |    0 
     |    |
     |  
     |
     |
    [_]""")
        if guesses_left == 1:
            print("""      ____
     |    |
     |   _0_  
     |  | | |
     |  
     |
     |
    [_]""")

        #uzprinte dashus
        print("")
        print(dashes)
        print("")

        #parada cik tev ir dzivibas
        print ("lives",str(guesses_left))
        
        #minejums, inputs
        guess = input("Guess:")
        
        #ja minekums nebus 1 caracteris vins tev liks ievadit vienu
        if len(guess) != 1:
          print("")
          print ("Your guess must have exactly one character!")
          
        #saprot ko darit ja minejums ir vai nav varda
        elif guess in secret_word:
          print("")
          print (guess, " is in the secret word!")
          dashes = update_dashes(secret_word, dashes, guess)
          
        else:
          print("")
          print (guess, " is not in the secret word!")
          guesses_left -= 1
        
      #ja nav vairak dzivibu tad spele beidzas un vins parada vardu
      if guesses_left < 1:
        print("-------------------------------------------------")
        print ("You lose. The word was: " + str(secret_word))
        print("-------------------------------------------------")
        lvl = lvl-5
      
      #ja limenis bus mazaks par pieci, pabeidzot to vins tevi aizmetis uz nakosos limeni
      else:
        if lvl < 5:
          print("-------------------------------------------------")
          print ("You move on. The word was: " + str(secret_word))
          print("-------------------------------------------------")
          lvl = lvl+1
        #ja tu pabeidz piekto limeni tad vins tevi apsveic ar uzvaru
        else:
          print("///////////////")
          print("")
          print("You won!")
          print("")
          print("///////////////")
          break

    #ja tev dzivibas ir mazak vai vienads par viens tad vins tev parada final karatavas veciti un pasaka kad tu esi zaudejis
    if lvl <= 1:
      print("""      ____
     |    |
     |   _0_  
     |  |_|_|
     |  |   |
     |
     |
    [_]""")
      print("///////////////")
      print("")
      print("You lose!")
      print("")
      print("///////////////")
      break

  #apstadina laiku un parada kads bija tavs laiks
  end_time = time.time()
  laiks = int(end_time - start_time)
  #parada tavu laiku un scoru
  print(name, "your time was : ", laiks, "sec")
  score = int(1000/laiks*guesses_left)
  print("And your score is ",score)

  #atkartojuma funkcija
  atkartojums = input("Do you want to try again (Y/N) : ").lower()
  if atkartojums == "y":
    get_guess()
  else:
    print("Have a nice day!")

#dashu update kods
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess
      
    else:
      result = result + cur_dash[i]
      
  return result

#vardu bankas
words1 = ["viens", "viens", "viens"]
words2 = ["divi", "divi"]
words3 = ["tris", "tris"]
words4 = ["cetri", "cetri"]
words5 = ["pieci", "pieci"]

#randomizi izvilkt vardu no vardu bankas
secret_word1 = random.choice(words1)
secret_word2 = random.choice(words2)
secret_word3 = random.choice(words3)
secret_word4 = random.choice(words4)
secret_word5 = random.choice(words5)

get_guess()

