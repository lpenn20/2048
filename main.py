from GameState import GameState
from collections import deque
from RandomHelpers import oneOutOfN
from PlayGame import *
import unittest
import random

game = GameState(4, 4, [deque([0,0,2,16]),
                        deque([0,0,2,16]),
                        deque([0,2,8,32]),
                        deque([0,2,4,64])])
game2 = GameState(4, 4)
game3 = GameState(10, 1)
autoPlay(game2, 4)
#playGame(game2)
#unittest.main('Game_Test')
