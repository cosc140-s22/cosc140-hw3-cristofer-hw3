#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################
import string 
import random 
def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist

  
def getLetter(player):
  letter=""
  playerNum= str(player)
  while letter=="":
    temp= input(f"Player {playerNum}, how about a letter: ")
    if temp.isalpha():
      letter = temp.upper()
    else:
      print("That is not a valid letter")
  return letter

  
def fragmentCheck(wordFragment,wordList):
  # returns true if the wordFragment starts one of the 
  # words in the list and false otherwise
  for word in wordList:
    if word.startswith(wordFragment.upper()):
      return True 
  return False 


  
def wordCheck(wordFragment, list):
  #returns true if player completed a word 
  #longer than 3 characters
  for word in list:
    if wordFragment== word and len(word)>3:
      return True
  return False


  
def playGame():
  play= True
  fragment=""
  list=load_wordlist()
  while play:
    one= getLetter(1)
    fragment+=one
    print(f"Player 1 chose {one}, giving the fragment {fragment}. ")
    if not fragmentCheck(fragment,list) or wordCheck(fragment,list):
      print("Player 1 just lost")
      play=False
      break
    two=getLetter(2)
    fragment+=two
    print(f"Player 2 chose {two}, giving the fragment {fragment}. ")
    if not fragmentCheck(fragment,list) or wordCheck(fragment,list):
      print("Player 2 just lost")
      play=False
      break

def playGameCPULOW():# low level cpu player program 
  words= string.ascii_letters
  play= True
  fragment=""
  list=load_wordlist()
  while play:
    one= getLetter(1)
    fragment+=one
    print(f"Player 1 chose {one}, giving the fragment {fragment}. ")
    if not fragmentCheck(fragment,list) or wordCheck(fragment,list):
      print("Player 1 just lost")
      play=False
      break
    cpu=random.choice(words).upper()
    fragment+=cpu
    print(f"CPU(low) chose {cpu}, giving the fragment {fragment}. ")
    if not fragmentCheck(fragment,list) or wordCheck(fragment,list):
      print("CPU just lost")
      play=False
      break
      
def main():
    words = load_wordlist()
    print(f"{len(words)} words loaded.")

    # you can start your code here, inside main
    print("******Welcome to Ghost PY!*******")
    #playGame()
    playGameCPULOW()
    
#For the difficult player to play agaisnt I am thinking having the player chose a random letter from letters that will continue to make words, so search through the remaining words that start with the fragment, allocate those letters and have the cpu chose from those.
main()
