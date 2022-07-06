import sys


class ToyBot:

	x_axis = list(range(0, 5))
	y_axis = list(range(0, 5))

	def __init__(self):
		self.actions = {
			'place': self.place, 'move': self.move, 'report': self.report,
			'left': self.left, 'right': self.right,
		}
		self.current_x_pos = 0
		self.current_y_pos = 0
		self.current_facing = ''

	def validate_place(self, x, y, facing):
		valid = False
		facings = ['NORTH', 'SOUTH', 'WEST', 'EAST']
		if not x.isdigit():
			print(f'First value must be a valid number. You entered {x}')
		elif int(x) >= len(self.x_axis):
			print(f'First value must be less than {len(self.x_axis)} or else '
				  f'the bot will fall. You entered {x}')
		elif not y.isdigit():
			print(f'Second value must be a valid number. You entered {y}')
		elif int(y) >= len(self.y_axis):
			print(f'Second value must be less than {len(self.y_axis)} or else '
				  f'the bot will fall. You entered {y}')
		elif facing.upper() not in facings:
			print(f'Third value is invalid. Choices are {",".join(facings)}. '
				  f'You entered {facing}')
		else:
			valid = True
		return valid

	def place(self, x, y, facing):
		"""
		:param x: initial position on the x-axis
		:param y: initial position on the y-axis
		:param facing: initial facing position
			- e.g. NORTH, SOUTH, EAST, WEST
			- note: West is left as East is righ
		"""
		if not self.validate_place(x, y, facing):
			return False
		self.current_x_pos = int(x)
		self.current_y_pos = int(y)
		self.current_facing = facing.upper()
		return True

	def move(self):
		if self.current_facing in ['NORTH', 'SOUTH']:
			if self.current_y_pos < len(self.y_axis):
				self.current_y_pos += 1
		elif self.current_facing in ['WEST', 'EAST']:
			if self.current_x_pos < len(self.x_axis):
				self.current_x_pos += 1

	def left(self):
		change_positions = {'NORTH': 'WEST', 'SOUTH': 'EAST',
							'WEST': 'SOUTH', 'EAST': 'NORTH'}
		self.current_facing = change_positions[self.current_facing]

	def right(self):
		# The tricky part
		change_positions = {'NORTH': 'EAST', 'SOUTH': 'WEST',
							'WEST': 'NORTH', 'EAST': 'SOUTH'}
		self.current_facing = change_positions[self.current_facing]

	def report(self):
		# End
		print(f'{self.current_x_pos},'
			  f'{self.current_y_pos},'
			  f'{self.current_facing}')


print('====TOYBOT CONSOLE APPLICATION====')
bot = ToyBot()
placed = False
while not placed:
	starting_place = input('STARTING PLACE(e.g. 0,0,NORTH): ')
	place = starting_place.replace(' ', '').split(',')
	placed = bot.place(place[0], place[1], place[2])
next_action = ''
while next_action.lower() != 'report':
	next_action = input(
		'PLEASE INPUT NEXT ACTION(e.g. PLACE, MOVE, REPORT, LEFT, RIGHT): '
	)
	_next_action = next_action.lower()
	if _next_action == 'place':
		starting_place = input('IMMEDIATE PLACING(e.g. 0,0,NORTH): ')
		place = starting_place.replace(' ', '').split(',')
		placed = bot.place(place[0], place[1], place[2])
	elif bot.actions.get(_next_action):
		bot.actions[next_action.lower()]()
	else:
		print(f'You have input a wrong action: {next_action}')

# # TEST 1: 0,1,NORTH
# bot = ToyBot()
# bot.place(0, 0, 'NORTH')
# bot.move()
# bot.report()
#
# # TEST 2: 0,0,WEST
# bot = ToyBot()
# bot.place(0, 0, 'NORTH')
# bot.left()
# bot.report()
#
# # TEST 3: 3,3,NORTH
# bot = ToyBot()
# bot.place(1, 2, 'EAST')
# bot.move()
# bot.move()
# bot.left()
# bot.move()
# bot.report()
