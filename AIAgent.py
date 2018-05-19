from keras.models import Sequential
from keras.layers import Dense, Activation
from player import Player
import numpy as np
from keras import backend as K
import tensorflow as tf
from functools import reduce

def custom_loss(y_true,y_pred):
  A = y_true
  #indicates good or bad game depending on if A is negative or positive
  return A * K.log(y_pred)


class AIAgent(Player):
  def setupNet(self):
    self.model = Sequential([
        Dense(200, input_dim=100**2),
        Activation('relu'),
        Dense(1),
        Activation('sigmoid'),
    ])

    self.model.compile(optimizer='rmsprop',
                  loss=custom_loss,
                  metrics=['accuracy'])

  def trainOnEpisode(self, episode,ep_num):
    #episode is a list of 30 tuples [(game_history_array, #times_hit)]
    #game_history_array is a list of tuples (game_state, action_sampled)
    #need to compute differences --> let loss = #times_hit
    train_x = []
    train_y = []
    for hist, times_hit in episode:
      game_states_temp = list(map(lambda x: x[0], hist))
      game_states = []
      for i in range(0,len(game_states)-1):
        game_states = game_states_temp[i+1] - game_states_temp[i]
      if(len(train_x) == 0):
        train_x = game_states
      else:
        train_x = np.vstack([train_x,game_states])
      train_y = np.append(train_y,np.array([-1 * times_hit for tup in hist]))
    self.model.train_on_batch(train_x,train_y)
    self.model.save('models/model'+str(ep_num))
  
  def makeSmartMove(self, screenshot):
    pred = self.model.predict(screenshot)[0][0]
    if(pred > 0.5):
      self.move("RIGHT")
      return 1
    else:
      self.move("LEFT")
      return -1