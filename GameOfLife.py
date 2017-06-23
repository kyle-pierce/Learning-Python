import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255			# default color of an ON location
OFF = 0				# default color of an OFF location
vals = [ON, OFF]	# values for each location

def random_grid(n):
	"""returns a grid of n x n random values"""
	return np.random.choice(vals, n * n, p = [0.2, 0.8]).reshape(n, n)

def add_glider(i, j, grid):
	"""adds a 3 x 3 glider with top left cell at (i, j) to the given grid"""
	glider = np.array([[0,   0,   255], 
					   [255, 0,   255],
					   [0,   255, 255]])
	grid[i : i + 3, j : j + 3] = glider

def update(frame_num, img, grid, n):
	"""updates the values in the current grid using Conway's rules"""

	# copy the grid so we can update an index as soon as calculating neighbors
	new_grid = grid.copy()

	# for each index, total the ON neighbors and add value to the new grid
	for i in range(n):
		for j in range(n):
			# sum the neighbors (number of ON neighbors)
			total = sum_neighbors(grid, i, j, n)

			# apply Conway's rules of life
			if (grid[i, j] == ON):
				# over/underpolulation kills 
				if (total < 2) or (total > 3):
					new_grid[i, j] = OFF
			else:
				# normal population -> prosperous
				if total == 3:
					new_grid[i, j] = ON

	# update the image and grid data
	img.set_data(new_grid)
	grid[:] = new_grid[:]

	return img

def sum_neighbors(grid, i, j, n):
	"""returns the total number of ON neighbors of grid[i, j] of size n x n"""
	total = int((grid[i, (j - 1) % n] + grid[i, (j + 1) % n] +
		         grid[(i - 1) % n, j] + grid[(i + 1) % n, j] +
		         grid[(i - 1) % n, (j - 1) % n] + grid[(i - 1) % n, (j + 1) % n] +
		         grid[(i + 1) % n, (j - 1) % n] + grid[(i + 1) % n, (j + 1) % n]) / 255)
	return total;

def add_arguments(parser):
	"""adds the expected arguments to the parser"""
	parser.add_argument('--grid-size', dest = 'n', required = False)
	parser.add_argument('--mov-file', dest = 'mov_file', required = False)
	parser.add_argument('--interval', dest = 'interval', required = False)
	parser.add_argument('--glider', action = 'store_true', required = False)

def initialize_grid(glider, n):
	"""returns either a random or glider n x n grid"""
	grid = np.array([])

	# use glider if specified, random otherwise
	if (glider):
		grid = np.zeros(n * n).reshape(n, n)
		add_glider(1, 1, grid)
	else:
		grid = random_grid(n)

	return grid

def initialize_animation(grid, update_interval, n):
	"""initialized the animation using the grid, update interval, and grid size"""
	fig, ax = plt.subplots()
	img = ax.imshow(grid, interpolation = 'nearest')
	return animation.FuncAnimation(fig, update, fargs = (img, grid, n, ), frames = 10,
								 	   interval = update_interval, save_count = 50)

def main():
	# command line arguments are in sys.argv[1], sys.argv[2] ...
	# sys.argv[0] is the name of the script, which is not needed

	# parse arguments
	parser = argparse.ArgumentParser(description = "Runs Conway's Game of Life simulation")

	# add and retrieve arguments
	add_arguments(parser)
	args = parser.parse_args()

	# set the size of the grid with default 100
	n = 100
	if (args.n) and (int(args.n) > 8):
		n = int(args.n)

	# set the animation update interval with default 50
	update_interval = 50
	if (args.interval):
		update_interval = args.interval

	# declare the grid
	grid = initialize_grid(args.glider, n)

	# set up the animation
	ani = initialize_animation(grid, update_interval, n)

	# set the output file
	if (args.mov_file):
		ani.save(args.mov_file, fps = 30, extra_args = ['-vcodec', 'libx264'])

	plt.show()

# calls the main method
if __name__ == '__main__':
	main()