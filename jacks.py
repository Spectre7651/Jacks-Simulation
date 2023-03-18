#
#Make it so that when a card is played it is revoved from the array before comp.
#
#Imports
def jacks():
  import random
  from time import sleep

  #Declares the deck of cards (std 52 card)
  deckofcards = ["A","A","A","A","2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","T","T","T","T","J","J","J","J","Q","Q","Q","Q","K","K","K","K"]

  #Shuffle the deck
  random.shuffle(deckofcards)

  #Split the deck between the players
  def split(deckofcards):
    player1 = []
    player2 = []
    for i in range(len(deckofcards)):
      if (i % 2) == 0:
        player2.append(deckofcards[i])
      else:
        player1.append(deckofcards[i])
    print(len(player1))
    print(len(player2))
    return player1, player2
  #Main
  player1, player2 = split(deckofcards)
  i = 1
  playerturn = 1
  pile = []
  while len(player1) > 0 and len(player2) > 0:
    i = 0
    if len(player1) == 0:
        break
    if len(player2) == 0:
        break
    while playerturn == 1: #Player 1 turn.
      fcp1=0
      print("1")
      #i = (i + 1)
      i = 0
      cardplayed = player1[0]
      player1.pop(0)
      pile.append(cardplayed)
      sleep(1)
      #######
      #Jack #
      #######
      if cardplayed == "J":
        print("J")
        #If 2 doesn't play a face card the pile is appended to them if they do 2 become the player and the card is added to pile
        if player2[0] == "J" or player2[0] == "Q" or player2[0] == "K" or player2[0] == "A":
          playerturn = 2
          pile.append(player2[(i%len(player2))])
          player2.pop((i%len(player2)))
          sleep(1)
        else:
          player2 = player2 + pile
          pile = [] #Wipe pile
          playerturn = 2
          sleep(1)
      ########
      #Queen #
      ########
      elif cardplayed == "Q":
        print("Q")
        for i in range(2): #2 tries
          if player2[0] == "J" or player2[0] == "Q" or player2[0] == "K" or player2[0] == "A":
            playerturn = 2
            pile.append(player2[(i%len(player2))])
            player2.pop((i%len(player2)))
            sleep(1)
            break
          else: #If fail dont do anything
            fcp1 += 1
        if fcp1 == 2: #if playerturn has not changed it must have failed.
          player2 = player2 + pile
          pile = [] #Wipe pile
          playerturn = 2
          sleep(1)

      #######
      #King #
      #######
      elif cardplayed == "K":
        print("K")
        for i in range(3): #2 tries
          if player2[0] == "J" or player2[0] == "Q" or player2[0] == "K" or player2[0] == "A":
            playerturn = 2
            pile.append(player2[(i%len(player2))])
            player2.pop((i%len(player2)))
            sleep(1)
            break
          else: #If fail dont do anything
            fcp1 += 1
        if fcp1 == 3: #if playerturn has not changed it must have failed.
          player2 = player2 + pile
          pile = [] #Wipe pile
          playerturn = 2
          sleep(1)
      
      ######
      #Ace #
      ######
      elif cardplayed == "A":
        print("A")
        for i in range(4): #2 tries
          if player2[0] == "J" or player2[0] == "Q" or player2[0] == "K" or player2[0] == "A":
            playerturn = 2
            pile.append(player2[(i%len(player2))])
            player2.pop((i%len(player2)))
            sleep(1)
            break
          else: #If fail dont do anything
              fcp1 += 1
        if fcp1 == 4: #if playerturn has not changed it must have failed.
          player2 = player2 + pile
          pile = [] #Wipe pile
          sleep(1)
          playerturn = 2
          

      #######
      #Fail #
      #######
      else:
        print("O")
        playerturn = 2
        sleep(1)

  ###Player 2 turn
    while playerturn == 2: #Player 2 turn.
      i = 0
      fcp2 = 0
      print("2")
      #i = i+1
      print(player2)
      cardplayed = player2[0]
      player2.pop(0)
      pile.append(cardplayed)
      sleep(1)
      #######
      #Jack #
      #######
      if cardplayed == "J":
        print("2J")
        #If 2 doesn't play a face card the pile is appended to them if they do 2 become the player and the card is added to pile
        if player1[0] == "J" or player1[0] == "Q" or player1[0] == "K" or player1[0] == "A":
          playerturn = 1
          pile.append(player1[(i%len(player1))])
          player1.pop((i%len(player1)))
          sleep(1)
        else:
          player1 = player1 + pile
          pile = [] #Wipe pile
          playerturn = 1
          sleep(1)
      ########
      #Queen #
      ########
      elif cardplayed == "Q":
        print("2Q")
        for i in range(2): #2 tries
          if player1[0] == "J" or player1[0] == "Q" or player1[0] == "K" or player1[0] == "A":
            playerturn = 1
            pile.append(player1[(i%len(player1))])
            player1.pop((i%len(player1)))
            sleep(1)
            break
          else: #If fail dont do anything
            fcp2 += 1
        if fcp2 == 2: #if playerturn has not changed it must have failed.
          player1 = player1 + pile
          pile = [] #Wipe pile
          playerturn = 1
          sleep(1)

      #######
      #King #
      #######
      elif cardplayed == "K":
        print("2K")
        for i in range(3): #2 tries
          if player1[0] == "J" or player1[0] == "Q" or player1[0] == "K" or player1[0] == "A":
            playerturn = 1
            pile.append(player1[(i%len(player1))])
            player1.pop((i%len(player1)))
            sleep(1)
            break
          else: #If fail dont do anything
            fcp2 += 1
        if fcp2 == 3: #if playerturn has not changed it must have failed.
          player1 = player1 + pile
          pile = [] #Wipe pile
          playerturn = 1
          sleep(1)
      
      ######
      #Ace #
      ######
      elif cardplayed == "A":
        print("2A")
        for i in range(4): #2 tries
          if player1[0] == "J" or player1[0] == "Q" or player1[0] == "K" or player1[0] == "A":
            playerturn = 1
            pile.append(player1[(i%len(player1))])
            player1.pop((i%len(player1)))
            sleep(1)
            break
          else: #If fail dont do anything
            fcp2 += 1
        if fcp2 == 4: #if playerturn has not changed it must have failed.
          player1 = player1 + pile
          pile = [] #Wipe pile
          playerturn = 1
          sleep(1)

      #######
      #Fail #
      #######
      else:
        print("2O")
        playerturn = 1
        sleep(1)

jacks()