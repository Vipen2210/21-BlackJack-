import random
import time
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



class start_player():

	def __init__(self):
		pass
	def bio(self):
		global name 
		name = input('Enter your name:')
		print(f"Hello {name} !! ")
		print("welcome to Vipens casino:")

	def total_money(self):
		while True:
			try:
				total_money_for_bet=int(input('Your total balance sir:'))
				return total_money_for_bet
			except ValueError:
				print('Sorry, a bet must be an integer!')
			else:
				break

	def bet_money(self):
		while True:
			try:
				money_for_bet=int(input('Your bet sir:'))
				return money_for_bet
			except ValueError:
				print('Sorry, a bet must be an integer!')
			else:
				break
class cards():

	def __init__(self,suits,ranks):
		self.suits=suits
		self.ranks=ranks
	
	def show_rank(self):
		return self.ranks
	def show(self):
		return f"{self.ranks} of {self.suits}"
class check_total():

	def __init__(self,turn):

		self.turn = turn
		self.value = 0
		self.aces = 0
	
	def sum_on_cards(self):

		for i in range(self.turn):
			t= player_c1.show_rank()
			self.value += values[t]	
			print(self.value)	

class hand(cards):

		def __init__(self):
			 
			self.player_deck=[]
			self.computer_deck=[]

		def player_addcards(self):
			test=(random.choice(suits),random.choice(ranks))
			self.player_deck.append(test)
			return f'{test[1]} of {test[0]}'
		def computer_addcards(self):
			test=(random.choice(suits),random.choice(ranks))
			self.computer_deck.append(test)
			return f'{test[1]} of {test[0]}'

player_s1 = start_player()
player_s1.bio()


# print(total_bet)

# print(total_bank_balance)


# for taking the list of players

# print(h1.player_deck[1][1]) 
# print(h2.computer_deck)

def game():
	total_bet=player_s1.bet_money()
	total_bank_balance=player_s1.total_money()
	if total_bet>total_bank_balance:
		play_again=False
		print('Sorry you cant play anymore')

	else:
		play_again=True
		h1=hand()
		h2=hand()

		print('\n')
		print(f'{name} hand.........:')
		player=[h1.player_addcards(),h1.player_addcards()]
		print(player)

		print('\n')
		print('Dealers hand.........:')

		computer=[h2.computer_addcards()]
		print(computer)
		
		playing = True
		while playing:
			while playing:
				try:
					print("Would you like to Hit or Stand? Enter 'h' or 's' :----:")
					choice = input()
					choice.lower()
				except:
					print('please enter the h or s')


				for i in range(1):

					if choice == 'h':
						player.append(h1.player_addcards())
						print(player)
						t=0
						r=0
						for j in range(len(h2.computer_deck)):
							sum_of_ccards=h2.computer_deck[j][1]
							r += values[sum_of_ccards]
						for j in range(len(h1.player_deck)):
							sum_of_pcards=h1.player_deck[j][1]
							t += values[sum_of_pcards]
						
						if t<21:
							# player.append(h1.player_addcards())
							# print(player)
							break
						elif t>=21:
							for j in range(len(h2.computer_deck)):
								if h2.computer_deck[j][1] == 11:
									h2.computer_deck[j][1] = 1
									sum_of_ccards=h2.computer_deck[j][1]
									r += values[sum_of_ccards]
								else:
									
									playing=False
									
									total_bank_balance+=total_bet
									print("PLayer Wins")
									break
						else:
							print('you are busted')
							print("YOU LOOSE")
							total_bank_balance-=total_bet
							playing=False
							break



							
					elif choice == 's':
						
						r=0
						t=0
						computer.append(h2.computer_addcards())
						print(computer)

						for j in range(len(h1.player_deck)):
							sum_of_pcards=h1.player_deck[j][1]
							t += values[sum_of_pcards]
						
						for j in range(len(h2.computer_deck)):
							sum_of_ccards=h2.computer_deck[j][1]
							r += values[sum_of_ccards]
						
						if t<r and r>17:
							print("Computer wins")
							total_bank_balance-=total_bet
							playing=False
							break

						elif t>r and r>17:
							print("Player Wins the game")
							total_bank_balance+=total_bet
							print("Congoratulations !!!")
							playing=False
							break

						elif r>=21:
							for j in range(len(h2.computer_deck)):
								if h2.computer_deck[j][1] == 11:
									h2.computer_deck[j][1] = 1
									sum_of_ccards=h2.computer_deck[j][1]
									r += values[sum_of_ccards]
								else:
									
									playing=False
									
									total_bank_balance+=total_bet
									print("PLayer Wins")
									break

							if r<17:
								computer.append(h2.computer_addcards())
								print(computer)
							elif t>r and t<21 and r>17:
								print('PLAYER WINS THE GAME')
								total_bank_balance+=total_bet
								playing=False
								break
							elif t<r and t<21 and r>17:

								playing=False
								total_bank_balance-=total_bet
								print('computer WINS THE GAME')
								break
						elif r<17:
								computer.append(h2.computer_addcards())
								print(computer)
						
						
				
					# computer.append(h2.computer_addcards())
					# print(computer)
			else:
				playing=False

				break



game()

print('Do you want to play again ')
print('if yess press:1')
print('if no press:0')
play_again=int(input())



while play_again:
	# player_s1.bet_money()
	# player_s1.total_money()
	# if player_s1.total_money()<player_s1.bet_money():
	play_again=True
	# print('sorry you cant play')
	game()
	# else:
	# 	play_again=True
	# 	game()

	
else:
	print('by by')
