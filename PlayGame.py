from RandomHelpers import *
import math

def canPutBiggestInCorner(game):
  line1 = game.board[0].copy()
  line2 = game.board[-1].copy()
  for i in range(line1.count(0)):
    line1.remove(0)
  for i in range(line2.count(0)):
    line2.remove(0)
  if len(line1) == 0:
    line1.append(0)
  if len(line2) == 0:
    line2.append(0)
  if game.biggest in [line1[0],line1[-1],line2[0],line2[-1]]:
    return True
  return False
    
def score(game):
    game.updateAvailable()
    output = len(game.emptySpaces) * math.sqrt(game.biggest) * 0.55

    for line in game.board + game.columns:
        for i in range(len(line) - 1):
            if line[i] != 0:
                if line[i] == line[i + 1]:
                    output += math.sqrt(line[i])
                elif line[i] == line[i + 1] // 2:
                    output += math.sqrt(line[i]) * 0.4
                elif line[i] < line[i + 1]:
                    output += math.sqrt(line[i]) * 0.2

    if game.biggest == game.board[-1][-1]:
        output += 10000

    for num in game.biggestNums:
        if num in (game.board[0] + game.board[-1] + game.columns[0] + game.columns[-1]):
            if num not in game.corners and num != 0:
                output += math.sqrt(num) * 4

    output += game.biggest * 0.55

    snake_bonus = 0
    snake_multiplier = 2
    is_snake = check_snake_pattern(game.board)

    if is_snake:
        for row in game.board:
            for value in row:
                if value != 0:
                    snake_bonus += math.sqrt(value)
        snake_bonus *= snake_multiplier

    output += snake_bonus
    return int(output / 10)

def check_snake_pattern(board):
    for row in range(len(board)):
        for col in range(len(board[row]) - 1):
            if row % 2 == 0:
                if board[row][col] > board[row][col + 1] and board[row][col + 1] != 0:
                    return False
            else:
                if board[row][col] < board[row][col + 1] and board[row][col] != 0:
                    return False
    return True

def validMove(game, move):
  game_ = game.copy()
  if move == 'left':
    game_.moveLeft()
  if move == 'right':
    game_.moveRight()
  if move == 'down':
    game_.moveDown()
  if move == 'up':
    game_.moveUp()
  return game_.board != game.board

def availableMoves(game):
  moves = ['left', 'right', 'up', 'down']
  output = []
  for move in moves:
    if validMove(game, move):
      output.append(move)
  return output

def endGame(game):
  return availableMoves(game) == []

def bestMove(game, depth, player):
  # 1 = player, 2 = random num
  output = {}
  if player == 1:
    for move in availableMoves(game):
      game_ = game.copy()
      if endGame(game):
        depth == 1
      if move == 'left':
        game_.moveLeft()
      if move == 'right':
        game_.moveRight()
      if move == 'down':
        game_.moveDown()
      if move == 'up':
        game_.moveUp()
      game_.updateAvailable()
      if depth == 1:
        output[move] = score(game_)
      else:
        output[move] = bestMove(game_, depth-1, 2)[1]

  if player == 2:
    for move in game.emptySpaces:
      game_= game.copy()
      game_.addNum(2, move)
      game_.updateAvailable()
      if endGame(game_):
        depth = 1
      if depth == 1:
        output[move] = score(game_)
      else:
        output[move] = bestMove(game_, depth-1, 1)[1]
  if depth == 4:
    print(output)
    
  if player == 1:
    return maxValue(output)
  
  else:
    return (0, averageValue(output))


def playGame(game):
  print(f'{game}\n')
  move = input('what is your move?\n')
  if move == 'break':
    return 'break'
  if validMove(game, move):
    if move == 'left':
      game.moveLeft()
    if move == 'right':
      game.moveRight()
    if move == 'down':
      game.moveDown()
    if move == 'up':
      game.moveUp()
    game.updateAvailable()
    game.addRandomNum()
    game.updateAvailable()
    print(f'you played: {move}')
    return playGame(game)
  else:
    print('invalid move')
    return playGame(game)

def autoPlay(game, depth):
  print(f'{game}\n')
  if endGame(game):
    return 'fail'
  move = bestMove(game, depth, 1)[0]
  print(f'move = {move}')
  if move == 'left':
    game.moveLeft()
  if move == 'right':
    game.moveRight()
  if move == 'down':
    game.moveDown()
  if move == 'up':
    game.moveUp()
  game.updateAvailable()
  game.addRandomNum()
  game.updateAvailable()
  print(game.biggestNums)
  return autoPlay(game, depth)
