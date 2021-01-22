#%%
import numpy as np
import tensorflow as tf
import math
from tensorflow import keras
from tensorflow.keras import layers
#%%
def CreateLayer(layer):
    pass

InputNum = 16


'''
inp = []

for j in range(math.ceil(InputNum/2)):
    inp.append(keras.Input(shape = (int(InputNum/2),)))


per ogni layer parti dall'inizio e fai:
    se ci sono due layer disponibili:
        prendi i due output precedenti e fai concatenate
        applica dense
    se manca un layer:
        prendi l'ultimo layer disponibile e un layer a caso
        fai concatenate
        applica dense

'''

inp = keras.Input(shape=InputNum)

intermediate = []

for i in range(int(InputNum/2)-1):
    intermediate.append(Lambda(lambda x: x[:,i:i+2], output_shape=((2,))))












#x = layers.concatenate([title_features, body_features, tags_input])

'''
a = keras.Input(shape=(InputNum,))
b = keras.Input(shape=(InputNum,))

a1 = layers.Dense(1)(a)
b1 = layers.Dense(1)(b)
c = layers.concatenate([a1,b1])
z = layers.Dense(1)(c)

mod = keras.Model(
    inputs=[a,b],
    outputs=[z],
)

keras.utils.plot_model(mod, "ex_3.png", show_shapes=True)
'''
#%%


inputs = keras.Input(shape=(InputNum,), name="inp")
x = layers.Dense(InputNum)(inputs)
for i in range(3):
    x = layers.Dense(InputNum)(x)
outputs = layers.Dense(1, name="out")(x)


model = keras.Model(
    inputs=[inputs],
    outputs=[outputs],
)


#%%

keras.utils.plot_model(model, "ex_3.png", show_shapes=True)

#%%
