import pandas as pd
from sklearn import linear_model
import csv
from sklearn.preprocessing import Binarizer

# with open('cars.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Weight', 'Volume', 'price']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'Volume': 2300 , 'Weight': 1300, 'price': 20})

df = pd.read_csv('Paul Morphy vs Charles Le Carpentier _TEST.csv')
#we’re selecting the colums to binarize
WRa = df.iloc[:, 0].values
WNb = df.iloc[:, 1].values
WBc = df.iloc[:, 2].values
print("\nWRa ORG: ", WRa)
print("\nWNb ORG: ", WNb)
print("\nWBc ORG: ", WBc)

#now we turn them into values we can work with
X = WRa
X = X.reshape (1, -1)
Y = WNb
Y = Y.reshape (1, -1)
Z = WBc
Z = Z.reshape (1, -1)

#we need to set a threshold to define as 1 or 0
binarizer_X = Binarizer(0.1)
binarizer_Y = Binarizer(1)
binarizer_Z = Binarizer(2)
# finally we run the Binarizer function
print( "\nbinary WRa :\n", binarizer_X.fit_transform(X))
print( "\nbinary WNb :\n", binarizer_Y.fit_transform(Y))
print( "\nbinary WBc :\n", binarizer_Z.fit_transform(Z))


#
# df = pd.read_csv("check.csv")

x = df[['WRa', 'WNb','WBc',	'WQ', 'WK',	'WBf', 'WNg', 'WRh', 'WPa', 'WPb',\
'WPc', 'WPd', 'WPe', 'WPf', 'WPg', 'WPh', 'BRa', 'BNb', 'BBc', 'BQ',\
'BK', 'BBf', 'BNg', 'BRh', 'BPa', 'BPb', 'BPc',	'BPd', 'BPe', 'BPf', 'BPg', 'BPh']]

y = df['TF']

regr = linear_model.LinearRegression()
regr.fit(x, y)

predictedTF_1 = regr.predict(binarizer_X.fit_transform(X))
predictedTF_2 = regr.predict(binarizer_Y.fit_transform(Y))
predictedTF_3 = regr.predict(binarizer_Z.fit_transform(Z))

print(predictedTF_1)
print(predictedTF_2)
print(predictedTF_3)


#




# #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
# predictedprice = regr.predict([[42, 15]])
# #
# print(predictedprice)