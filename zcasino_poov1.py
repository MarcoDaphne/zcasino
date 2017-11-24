# -*- coding: utf-8 -*-
import random
import math

class Player:
	def __init__(self, wallet):
		self.wallet = wallet

	def want_to_quit(self):
		"""Method adding if the user want to quit"""
		answer = input('Voulez-vous vous retirer ? (y/n)')
		return True if answer == 'y' else False

class Croupier:
	def __init__(self, purse):
		self.purse = purse

	def get_choice(self):
		""" Request & Check, if the choice is in the range """
		ok = False
		while not ok:
			self.choice = int(input("Saisissez un nombre entre '0 et 49' (ex.30): "))
			if self.choice < 0 or self.choice > 49:
				self.choice = print("Vous avez saisie un nombre inférieur ou supérieur à la plage.\n")
			else:
				ok = True
		return self.choice

	def get_bid_on(self):
		""" Request & Check, if the bet is higher than the wallet"""
		ok = False
		while not ok:
			self.bet = int(input("Saisissez la valeur de votre mise (ex.99): "))
			if self.bet > self.purse.wallet:
				self.bet = print("La valeur de votre mise ne peut être plus grande que votre bourse.\n")
			else:
				ok = True
		return self.bet

	def winnings(self):
		"""Method calculating 3 times the bet and returning the earnings"""
		money = self.purse.wallet
		self.bet = self.bet * 3
		money += self.bet
		print("""
	Super !!!!
	Mais où avez vous caché votre trèfle à quatres feuilles !!!!
	Vous gagnez 3 fois votre mise.
		
		Gains : {} $         Portefeuille : {} $
			""".format(self.bet, money))
		return math.ceil(money)

	def earnings(self):
		"""Method calculating 50 % of the bet and returning the earnings"""
		money = self.purse.wallet
		self.bet = self.bet + (self.bet / 2)
		money += self.bet
		print("""
	Pas mal!! Vous gagnez '50 %' de votre mise.
		
		Gains : {} $         Portefeuille : {} $
			""".format(self.bet, money))
		return math.ceil(money)

	def losses(self):
		"""Method calculating the losses"""
		money = self.purse.wallet
		money -= self.bet
		print("""
	Dommage... Vous perdez votre mise.
	Retentez votre chance.
		
		Pertes : - {} $         Portefeuille : {} $
			""".format(self.bet, money))
		return math.ceil(money)

class GameTray:
	def __init__(self, player, croupier):
		self.player = player
		self.croupier = croupier

	def get_rand_numb(self):
		return random.randrange(50)

	def show_rand_numb(self):
		number = self.get_rand_numb()
		print("\nLa roulette renvoie le numéro {} .".format(number))
		return number

	def start(self):
		# boucle de jeu
		end = False
		while not end:
			choice = self.croupier.get_choice()
			bid_on = self.croupier.get_bid_on()
			returned_number = self.show_rand_numb()
			if (returned_number == choice):
				self.croupier.winnings()
			elif (returned_number % 2 == choice % 2 and returned_number % 1 == choice % 1):
				self.croupier.earnings()
			else:
				self.croupier.losses()
			end = self.player.want_to_quit()


def main():
	print("""
Bienvenue !!!
Nous allons jouer à 'ZCASINO'.
		
C'est facile, vous choisissez un nombre entre '0 et 49' puis vous misez, et c'est parti !!!
Pour éviter les excès(ex.1 000 000 $), nous avons limités votre portefeuille à '200 $'.
	""")
	user = Player(200)
	manager = Croupier(user)
	game = GameTray(user, manager)
	game.start()



main()

