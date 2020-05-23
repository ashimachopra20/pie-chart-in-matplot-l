import pandas as pd  
import numpy as np
dataset= pd.read_excel("#") 
print(dataset.dtypes)
temp = dataset.values
type(temp)
features = dataset.iloc[:, 1: ].values
labels = dataset.iloc[:, 0].values
dataset.isnull().any(axis=0)
print(dataset.dtypes)






from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)




from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)



print(regressor.intercept_)   
print (regressor.coef_)

Pred = regressor.predict(features_test)

import pandas as pd
import numpy as np
print (pd.DataFrame(zip(Pred, labels_test)))






x = [66,60]

x = np.array(x)
x = x.reshape(1, 2)
y=regressor.predict(x)
print("the height of the child predicted by given data of mom and dad height is:")
print(y)
Score = regressor.score(features_train, labels_train)
Score = regressor.score(features_test, labels_test)
print(Score)



