import unittest
from GameState import GameState
from collections import deque

class scoreTest(unittest.TestCase):
  def test1(self):
    game = GameState(4, 1, [deque([2,2,0,4])])
    game.makeMove('left')
    self.assertEqual(game.board, [deque([4, 4, 0, 0])])

  def test2(self):
    game = GameState(4,1, [deque([2,2,0,4])])
    game.makeMove('right')
    self.assertEqual(game.board, [deque([0, 0, 4, 4])])
