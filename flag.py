from emblem import Emblem
from board import Board

class Flag:
	def __init__(self):
		self.board = Board()
		initial = (0, 1, 2, 2)
		self.initial = Emblem(initial)

	def add_emblem(self, emblem, position):
		assert type(position) == type(())
		self.board[position[0]][position[1]]



if __name__ == '__main__':
	flag = Flag()
	print(flag.initial)