from keras.models import Sequential
from keras.layers import Dense, Activation
from player import Player
import numpy as np
from keras import backend as K
import tensorflow as tf

def custom_loss(y_true,y_pred):
  A = abs(y_pred[0])
  #indicates good or bad game
  if y_pred[0]/A != y_true[0]:
    return K.sum(tf.map_fn(lambda x: -1 * x , K.log(y_pred)))
  else: 
    return K.sum(K.log(y_pred))


class AIAgent(Player):
  def setupNet(self):
    self.model = Sequential([
        Dense(200, input_shape=(100**2,)),
        Activation('relu'),
        Dense(1),
        Activation('sigmoid'),
    ])

    self.model.compile(optimizer='rmsprop',
                  loss=custom_loss,
                  metrics=['accuracy'])

  def trainOnEpisode(self, episode):
    #episode is a list of 20 tuples (game_history_array, #times_hit)
    #game_history_array is a list of tuples (game_state, action_sampled)
    #need to compute differences --> let loss = #times_hit
    
    pass
  
  def makeSmartMove(self, screenshot):
    pred = self.model.predict(screenshot)[0][0]
    if(pred > 0.5):
      self.move("RIGHT")
      return 1
    else:
      self.move("LEFT")
      return -1