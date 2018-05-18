import numpy as np
import pygame

def oneOrZero(num):
  return 1 if num > 0 else 0

def getGameStateArray(surface):
  arr = [[oneOrZero(y) for y in x] for x in pygame.surfarray.array2d(surface)]
  arr = np.array(arr)
  arr = arr.T
  arr = arr.reshape((1,len(arr)**2))
  return arr


def getGameStateArray2d(surface):
  arr = [[oneOrZero(y) for y in x] for x in pygame.surfarray.array2d(surface)]
  arr = np.array(arr)
  arr = arr.T
  return arr

def writeGameStateArray(arr, i):
  f = open('/Users/niharpatil/Desktop/rlgame/states/state' + str(i) + '.txt', 'w+')
  arr_c = [[oneOrZero(y) for y in x] for x in arr]
  for row in arr_c:
    for col in row:
      f.write(str(col))
    f.write('\n')
  f.close()