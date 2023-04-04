import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

iris=pd.read_csv('Iris.csv')
x=iris.drop('Species',axis=1)
x=x.drop('Id',axis=1)
y=iris['Species']

le=LabelEncoder()
y=le.fit_transform(y)

x=np.array(x)

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.2,random_state=7)

log=LogisticRegression()
log.fit(xtrain,ytrain)

pickle.dump(log,open('iriss.pkl','wb'))
