# -*- coding: utf-8 -*-
import random
import math

class Player:
	def __init__(self, wallet):
		self.wallet = wallet

	def choose(self):
		""" Request & Check, if the choice is in the range """
		ok = False
		while not ok:
			self.choice = int(input("Saisissez un nombre entre '0 et 49' (ex.30): "))
			if self.choice < 0 or self.choice > 49:
				self.choice = print("Vous avez saisie un nombre inférieur ou supérieur à la plage.\n")
			else:
				ok = True
		return self.choice

	def bet(self):
		""" Request & Check, if the bet is higher than the wallet"""
		ok = False
		while not ok:
			self.bet = int(input("Saisissez la valeur de votre mise (ex.99): "))
			if self.bet > self.wallet:
				self.bet = print("La valeur de votre mise ne peut être plus grande que votre bourse.\n")
			else:
				ok = True
		return self.bet

	def want_to_quit(self):
		answer = input('Voulez-vous vous retirer ? (y/n)')
		return True if answer == 'y' else False

class GameTray:
	def __init__(self, player):
		self.player = player

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
			money = self.player.wallet
			choice = self.player.choose()
			bid_on = self.player.bet()
			returned_number = self.show_rand_numb()
			if (returned_number == choice):
				bid_on = bid_on * 3
				money = money + bid_on
				print("Super !!!!\nMise : + {} $    -    Bourse : {} $".format(bid_on, money))
			elif (returned_number % 2 == choice % 2 and returned_number % 1 == choice % 1):
				bid_on = bid_on + (bid_on / 2)
				money = money + bid_on
				print("Pas Mal !!\nMise : + {} $    -    Bourse : {} $".format(bid_on, money))
			else:
				money = money - bid_on
				print("Dommage...\nMise : - {} $    -    Bourse : {} $".format(bid_on, money))
			end = self.player.want_to_quit()


def main():
	print("""
Bienvenue !!!
Nous allons jouer à 'ZCASINO'.
		
C'est facile, vous choisissez un nombre entre '0 et 49' puis vous misez, et c'est parti !!!
Pour éviter les excès(ex.1 000 000 $), nous avons limités votre bourse à '200 $'.
	""")
	user = Player(200)
	game = GameTray(user)
	game.start()



main()

