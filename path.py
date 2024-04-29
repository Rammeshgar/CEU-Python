import random


def get_random_maze(maze_lenght):
  """Generate random maze. Return the given lenght vector containing 0 or 1"""
  maze = random.choices([0, 1], k=maze_lenght)
  maze[0] = 1
  maze[-1] = 1
  print(f'The maze is {maze} with {len(maze)} elements')
  return maze


def check_maze(maze):
  """Check wheater the maze can be solved."""
  quality = True
  for i in range(0, len(maze) - 4):
    t_maze = maze[i:(i + 5)]
    if sum(t_maze) == 0:
      quality = False
    elif sum(t_maze) == 1 and t_maze[3] == 1:
      quality = False
  return quality


def get_paths(maze, jumps):

  if check_maze(maze) == False:
    return 'There is no solution'

  paths = []
  final_path = []

  # check the first steps and ad it into paths
  for jump in jumps:
    if maze[jump] == 1:
      paths.append([0, jump])

  # generating all the possible outcomes
  for path in paths:
    start_index = path[-1]
    for jump in jumps:
      t_path = path.copy()
      if start_index + jump >= len(maze) - 1:
        t_path.append(start_index + jump)
        # 0 index to 1 index, more readable result
        t_path = [x + 1 for x in t_path]
        final_path.append(t_path)
        
      elif maze[start_index + jump] == 1:
        t_path.append(start_index + jump)
        paths.append(t_path)
        
  min_number_of_steps = min([len(x) for x in final_path])
  min_number_vectors = [x for x in final_path if len(x) == min_number_of_steps]
  #print(f"The possible paths: {final_path}")
  print(f'The minimum number of steps: {min_number_of_steps-1}')

  print(f'The fastest paths are the followings: {min_number_vectors}')


get_paths(maze=get_random_maze(10), jumps=[1, 2, 3, 5])