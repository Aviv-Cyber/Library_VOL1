import pandas as pd

df = pd.read_csv(r"C:\Users\avivy\GitHub\Hacking 101\.CSV\Paths.csv", header=None)
A_col = df.iloc[:, 0].values
B_col = df.iloc[:, 1].values
C_col = df.iloc[:, 2].values
D_col = df.iloc[:, 3].values

print(D_col[4])

exit()
# for i in range(186):
#     print("start " + A_col[1] + str(i) + "\n" + "timeout /t 5")
