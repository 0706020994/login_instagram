import numpy as np 

def deeplearningmodel(xtrain,ytrain,xtest,ytest,numfeatures,numepochs):
   #tp iniitialise the model
    model =tf.keras.models.Sequential()
    #To add the input and hidden layers
    model.add(tf.keras.layers.Dense(64, activation='relu',inputshape =(numfeatures,)))
    model.ad(tf.keras.layers.Dense(64,activation= 'relu',))
    #add the output layer
    model.add(tf.keras.layers.Dense(1,activation='sigmoid'))
    #compile the model
    model.compile(optimizer='adam',loss = 'binary_crossentropy',metrics = ['accuracy'])
    #train the model
    model.fit(xtrain,ytrain,epochs=numepochs)
    testloss,testacc=model.evaluate(xtest,ytest)
    print('Test accuracy:',testacc)
    return model

deeplearningmodel(xtrain, ytrain, xtest, ytest, numfeatures, numepochs)