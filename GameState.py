from collections import deque
from RandomHelpers import oneOutOfN
import random

class GameState():
  
  def __init__(self, width, height, board = None):
    self.width = width
    self.height = height
    self.board = board or [deque([0 for i in range(width)]) for i in range(height)]
    self.emptySpaces = []
    self.columns = [deque([0 for i in range(height)]) for i in range(width)]
    self.biggest = 2
    self.biggestNums = [0,0,0,0]
    self.corners = []
    self.recentlyAdded = (0,0)
    
    for r in range(self.height):
      for c in range(self.width):
        if self.board[r][c] == 0:
          self.emptySpaces.append((r,c))
          
    if len(self.emptySpaces) == height*width:
      for i in range(2):
        choice = random.choice(self.emptySpaces)
        self.emptySpaces.remove(choice)
        self.board[choice[0]][choice[1]] = 2
        
    for c in range(self.width):
      for r in range(self.height):
        self.columns[c][r] = self.board[r][c]

    self.corners = [self.board[0][0], self.board[0][-1], 
                    self.board[-1][0], self.board[-1][-1]]
      
  def moveLeft(self):
    for line in self.board:
      for i in range(line.count(0)):
        line.remove(0)
      for c in range(len(line)-1):
        if line[c] == line[c+1]:
          line[c] += line[c+1]
          line[c+1] = -1
      for i in range(line.count(-1)):
        line.remove(-1)
      for i in range(self.width-len(line)):
        line.append(0)
              
  def moveRight(self):
    for line in self.board:
      for i in range(line.count(0)):
        line.remove(0)
      m = [n for n in range(len(line)-1)]
      m.reverse()
      for c in m:
        if line[c+1] == line[c]:
          line[c+1] += line[c]
          line[c] = -1
      for i in range(line.count(-1)):
        line.remove(-1)
      for i in range(self.width-len(line)):
        line.appendleft(0)

  def moveDown(self):
    for line in self.columns:
      for i in range(line.count(0)):
        line.remove(0)
      m = [n for n in range(len(line)-1)]
      m.reverse()
      for c in m:
        if line[c+1] == line[c]:
          line[c+1] += line[c]
          line[c] = -1
      for i in range(line.count(-1)):
        line.remove(-1)
      for i in range(self.height-len(line)):
        line.appendleft(0)
    for c in range(self.width):
      for r in range(self.height):
        self.board[r][c] = self.columns[c][r]

  def moveUp(self):
    for line in self.columns:
      for i in range(line.count(0)):
        line.remove(0)
      for c in range(len(line)-1):
        if line[c] == line[c+1]:
          line[c] += line[c+1]
          line[c+1] = -1
      for i in range(line.count(-1)):
        line.remove(-1)
      for i in range(self.height-len(line)):
        line.append(0)
    for c in range(self.width):
      for r in range(self.height):
        self.board[r][c] = self.columns[c][r]
  
  def updateAvailable(self):
    for c in range(self.width):
      for r in range(self.height):
        self.columns[c][r] = self.board[r][c]
    self.emptySpaces = []
    for r in range(self.height):
      for c in range(self.width):
        if self.board[r][c] > self.biggest:
          self.biggest = self.board[r][c]
        if self.board[r][c] == 0:
          self.emptySpaces.append((r,c))
    self.corners = [self.board[0][0], self.board[0][-1], 
                    self.board[-1][0], self.board[-1][-1]]
    board = []
    for line in self.board:
      board += line
    for i in range(4):
      currentMax = max(board)
      self.biggestNums[i] = currentMax
      board.remove(currentMax)
  def addRandomNum(self):
    choice = random.choice(self.emptySpaces)
    if oneOutOfN(10):
      self.board[choice[0]][choice[1]] = 4
    else:
      self.board[choice[0]][choice[1]] = 2
    self.recentlyAdded = choice

  def addNum(self, num, pos):
    self.board[pos[0]][pos[1]] = num
    self.recentlyAdded = pos

  def copy(self):
    newBoard = []
    for line in self.board.copy():
      newBoard.append(line.copy())
    return GameState(self.width, self.height, newBoard)
  
  def __str__(self):
    output = ''
    strDict = {0: '0   ', 2: '2   ', 4: '4   ', 8: '8   ', 16: '16  ', 32: '32  ', 64: '64  ',
               128: '128 ', 256: '256 ', 512: '512 ', 1024: '1024', 2048: '2048', 
               4096: '4096', 8192 : '8192'
              }
    for h in range(self.height):
      output += '\n'
      for w in range(self.width):
        output += f'{strDict[self.board[h][w]]} '
    return output[1:]
