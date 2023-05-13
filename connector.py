# this module connects Simulator and Analysis to Software

# importing necessary modules
import pandas as pd
import numpy as np
from tensorflow import keras

# importing model
model = keras.models.load_model('models/version_0.3')

# importing simulator
import import_ipynb
import Simulator as s

# extraction of data necessary for normalization
class normalization_data():
     mean_and_std = pd.read_csv('data/normalization_data.csv')
     mean = np.array(mean_and_std['mean'])
     std = np.array(mean_and_std['std'])

# normalization function
def normalization(X):
     X -= normalization_data.mean
     X /= normalization_data.std
     return X

# function gets dataset for certain simulation and return prediction of its result from NN and from actual Simulator
def prediction_game(startNum, gVScRatio, lifespanSkinCells, civiliansProductivity, guardsProductivity, 
                    armyPriority, bacteriaStartPercent, takingFoodEffectivity, lifespanBacteria, 
                    chanceOfKillingGuard, chanceOfKillingCivilian):
    result = s.certain_simulation(startNum, gVScRatio, lifespanSkinCells, civiliansProductivity, 
                                  guardsProductivity, armyPriority, bacteriaStartPercent, takingFoodEffectivity, 
                                  lifespanBacteria, chanceOfKillingGuard, chanceOfKillingCivilian)
    x = np.array([[startNum, gVScRatio, lifespanSkinCells, civiliansProductivity, guardsProductivity, armyPriority, bacteriaStartPercent, 
                 takingFoodEffectivity, lifespanBacteria, chanceOfKillingGuard, chanceOfKillingCivilian]])
    prediction = model.predict(normalization(x))

    message1 = 'NN says: '
    message2 = 'Simulator says: '
    if prediction[0][1]>0.5:
          message1 += 'Bacteria will win.'
    else:
          message1 += 'Immunity will win.'
    if result == 1:
         message2 += 'Bacteria will win.'
    else:
         message2 += 'Immunity will win.'   
    return message1, message2 

# function runs random simulation, returns its params, result and prediction of its result from NN
def random_game():
     s.randomSimulation()
     s.beginSim()
     x = np.array([[s.gv.startNum, s.gv.gVScRatio, s.gv.lifespanSkinCells, s.gv.civiliansProductivity, s.gv.guardsProductivity, 
                    s.gv.armyPriority, s.gv.bacteriaStartPercent, s.gv.takingFoodEffectivity, s.gv.lifespanBacteria, 
                    s.gv.chanceOfKillingGuard, s.gv.chanceOfKillingCivilian]])
     X = np.copy(x)
     prediction = model.predict(normalization(x))
     final_pred = -1
     if prediction[0][1]>0.5:
          final_pred = 1
     else:
          final_pred = 0
     return X, s.gv.result, final_pred

