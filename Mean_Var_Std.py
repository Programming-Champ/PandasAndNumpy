#Python program by Brian Mageka to get mean, var, std, max, min and sum

import numpy as np

#Defining the funtion for calculation
def calculate(lst):
    before=np.array([lst])
    after=before.reshape((3,3))
    return( {'mean':[np.mean(after,axis=0).tolist(),np.mean(after,axis=1).tolist(),np.mean(after)],
    'variance' : [np.var(after,axis=0).tolist(),np.var(after,axis=1).tolist(),np.var(after)],
    'standard deviation' : [np.std(after,axis=0).tolist(),np.std(after,axis=1).tolist(), np.std(after)],
    'max' : [np.max(after,axis=0).tolist(),np.max(after,axis=1).tolist(),np.max(after)],
    'min' : [np.max(after,axis=0).tolist(),np.max(after,axis=1).tolist(),np.max(after)],
    'sum' : [np.sum(after,axis=0).tolist(),np.sum(after,axis=1).tolist(),np.sum(after)]
    })
#creating an empty list
a=[]

#number of elements as input
n=int(input("Enter number of elements: "))

#iterating to get values
for i in range(0,n):
    values=int(input())
    a.append(values)

print(a)
try:
    calculate(a)
except ValueError:
    print("List must contain nine numbers")
