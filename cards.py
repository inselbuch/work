from random import randint

class cards():

   def __init__(self):

      self.TRUMP = None

      self.SUITS = ['CLUBS','DIAMONDS','HEARTS','SPADES']
      self.POSITION = ['NORTH','WEST','EAST','SOUTH']
      self.RANKS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
      self.DECK = []
      self.HANDS = {}

      for suit in self.SUITS:
         for rank in self.RANKS:
            self.DECK.append([rank,suit])


   def swap(self,i,j):
      saveCard = self.DECK[j]
      self.DECK[j]=self.DECK[i]
      self.DECK[i] = saveCard


   def shuffle(self):
      for i in range(0,len(self.DECK)):
         self.swap(i,randint(0,len(self.DECK)-1))


   def deal(self,n):
      HAND = []
      while n > 0:
         HAND.append(self.DECK.pop())
         n=n-1

      HAND.sort(key=lambda item: (item[1],self.RANKS.index(item[0])))

      return HAND

   def deal_out(self, n_cards:int):
      for position in self.POSITION:
         self.HANDS[position] = self.deal(n_cards)

   def print_hand(self,position):

      # print trump first   
      if self.TRUMP != 'NO TRUMP':
         print(f"\t{self.TRUMP:<15}",end='')
         for card in self.HANDS[position]:
            if card[1] == self.TRUMP:
               print(f'{card[0]} ',end='')
         print()

      # now print each suit

      for suit in self.SUITS:
         if suit == self.TRUMP:
            continue

         print(f"\t{suit:<15}",end='')
         for card in self.HANDS[position]:
            if card[1] == suit:
               print(f'{card[0]} ',end='')
         print()

   def print_hands(self):
      for position in self.POSITION:
         print()
         print(position)
         self.print_hand(position)



if __name__ == "__main__":

   myDeck = cards()
   myDeck.shuffle()
   myDeck.deal_out(13)

   myDeck.TRUMP = 'NO TRUMP';
   trump = input("What is trump? (N,C,D,H,S) [N]: ") or "N"
   try:
      trump = str(trump)[0].upper()
      for suit in myDeck.SUITS:
         if trump == suit[0].upper():
            myDeck.TRUMP = suit
   except:
      pass

   print(f"Trump is {myDeck.TRUMP}")

   myDeck.print_hands()
