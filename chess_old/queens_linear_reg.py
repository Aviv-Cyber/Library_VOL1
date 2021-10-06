import pandas
from sklearn import linear_model
import csv

# with open('cars.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Weight', 'Volume', 'price']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'Volume': 2300 , 'Weight': 1300, 'price': 20})

df = pandas.read_csv("ctest.csv")
#
X = df[['Wqueen', 'Bqueen']]
y = df['TF']

regr = linear_model.LinearRegression()
regr.fit(X, y)
#

# #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedprice = regr.predict([[42, 15]])
#
print(predictedprice)