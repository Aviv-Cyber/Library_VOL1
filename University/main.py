import pandas as pd
import time as tm
import os
import subprocess


df = pd.read_csv(r"C:\Users\avivy\GitHub\my-app\.CSV\Cloud_Terms.csv", header=None)

A_col = df.iloc[:, 0].values  # Criteria
B_col = df.iloc[:, 1].values  # AWS
C_col = df.iloc[:, 2].values  # Azure
D_col = df.iloc[:, 3].values  # GCP
CP_list = [B_col, C_col, D_col]
A_List = A_col.tolist()
B_List = B_col.tolist()
C_List = C_col.tolist()
D_List = D_col.tolist()
os.chdir(r"C:\Users\avivy\GitHub\my-app\Directories\\")
parent_dir = os.getcwd()

# for x in B_col, C_col, D_col:
#     print(A_col[i] + ": " + x[i])
#     print("\n")

# for x in B_col, C_col, D_col:
#     print(A_col[i])

# listosh = A_col.tolist()
# for i in range(27):
#     print(listosh[i])

def CPD_func():
    for x in CP_list:
        directory = x[0]
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print("Directory '%s' created" % directory)


def CRT_func1(var1):
    for i in range(28):
        if A_List[i] != "CRITERIA":
            directory = A_List[i]
            path = os.path.join(parent_dir + "\\" + var1, directory)
            os.mkdir(path)
            # print("Directory '%s' created" % directory)
            print(path)
            file1 = B_List[i]+".bat"
            file2 = C_List[i]+".bat"
            file3 = D_List[i]+".bat"
            if B_List[0] in path:
                with open(os.path.join(path, file1), 'w') as fp:
                    pass
                    fp.write(path)
            if C_List[0] in path:
                with open(os.path.join(path, file2), 'w') as fp:
                    pass
                    fp.write(path)
            if D_List[0] in path:
                with open(os.path.join(path, file3), 'w') as fp:
                    pass
                    fp.write(path)


CPD_func()
for i in CP_list:
    CRT_func1(i[0])



