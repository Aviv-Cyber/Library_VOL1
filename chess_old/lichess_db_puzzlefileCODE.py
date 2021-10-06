import pandas as pd
from sklearn import linear_model
import csv
from sklearn.preprocessing import Binarizer
import ast

# with open('cars.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Weight', 'Volume', 'price']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'Volume': 2300 , 'Weight': 1300, 'price': 20})


def fishing(a, b, c):

    # choosing the CSV file
    df = pd.read_csv(a) # a is the file name
    # we’re selecting the colums to binarize
    TF = df.iloc[:, b].values # b is the colume number
    # showing what data we have seized from the CSV
    print("\nOriginal list : ", TF) # TF is the data from the colume
    # print("\nWRa ORG: ", WRa)
    # print("\nWNb ORG: ", WNb)
    # print("\nWBc ORG: ", WBc)


    #now we turn them into values we can work with
    # prepering the data for binarization
    XX = TF
    XX = XX.reshape (1, -1)
    # X = WRa
    # X = X.reshape (1, -1)
    # Y = WNb
    # Y = Y.reshape (1, -1)
    # Z = WBc
    # Z = Z.reshape (1, -1)
    #we need to set a threshold to define as 1 or 0

    # binaring the data
    binarizer_XX = Binarizer(c) # c is the zero point
    # binarizer_X = Binarizer(0)
    # binarizer_Y = Binarizer(1)
    # binarizer_Z = Binarizer(2)
    # finally we run the Binarizer function
    # print( "\nbinary TF :\n", binarizer_XX.fit_transform(XX))
    # print( "\nbinary WRa :\n", binarizer_X.fit_transform(X))
    # print( "\nbinary WNb :\n", binarizer_Y.fit_transform(Y))
    # print( "\nbinary WBc :\n", binarizer_Z.fit_transform(Z))

    # listing the data to a proper list
    TFBINARYSTR = (str(binarizer_XX.fit_transform(XX)))
    TFLISTbeta = TFBINARYSTR.replace('.',',')
    TFLISTALPHASTR = (TFLISTbeta[1:-1])
    TFLISTALPHALIST = ast.literal_eval(TFLISTALPHASTR)
    # counting and presenting the relevant data we wanted to exclude
    numero = ([i for i, n in enumerate(TFLISTALPHALIST) if n == 1])
    print(numero)
    print('add +2 to every int to get the excel line number')



# x = df[['TF']]
# y = df['TF']
# regr = linear_model.LinearRegression()
# regr.fit(x, y)
# predictedTF_0 = regr.predict(binarizer_XX.fit_transform(XX))
# predictedTF_1 = regr.predict(binarizer_X.fit_transform(X))
# predictedTF_2 = regr.predict(binarizer_Y.fit_transform(Y))
# predictedTF_3 = regr.predict(binarizer_Z.fit_transform(Z))
# print("\n")
# print(predictedTF_0)
# print(predictedTF_1)
# print(predictedTF_2)
# print(predictedTF_3)


# #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
# predictedprice = regr.predict([[42, 15]])

# print(predictedprice)

# choosing the CSV file
df = pd.read_csv('Paul Morphy vs Charles Le Carpentier _TEST.csv') # a is the file name
# we’re selecting the colums to binarize
TF = df.iloc[:, 1].values # b is the colume number
# showing what data we have seized from the CSV
print("\nOriginal list : ", TF) # TF is the data from the colume
XX = TF
XX = XX.reshape (1, -1)
# binaring the data
binarizer_XX = Binarizer(0)
# listing the data to a proper list
TFBINARYSTR = (str(binarizer_XX.fit_transform(XX)))
TFLISTbeta = TFBINARYSTR.replace('.',',')
TFLISTALPHASTR = (TFLISTbeta[1:-1])
TFLISTALPHALIST = ast.literal_eval(TFLISTALPHASTR)
# counting and presenting the relevant data we wanted to exclude
numero = ([i for i, n in enumerate(TFLISTALPHALIST) if n == 1])
print(numero)
print(type(numero))


fishing('against myself.csv', 1, 0)
fishing('Paul Morphy vs Charles Le Carpentier.csv', 1, 0)
