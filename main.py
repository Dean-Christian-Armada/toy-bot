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

	def place(self, x, y, facing):
		"""
		:param x: initial position on the x-axis
		:param y: initial position on the y-axis
		:param facing: initial facing position
			- e.g. NORTH, SOUTH, EAST, WEST
			- note: West is left as East is righ
		"""
		self.current_x_pos = x
		self.current_y_pos = y
		self.current_facing = facing.upper()

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
