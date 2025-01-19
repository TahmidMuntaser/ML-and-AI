import numpy as np

x = np.array([
    [0],
    [1]
])
y = np.array([1, 0])

w = np.array([0])
b = 0
alpha = 0.1


for epoch in range(20):
    for i in range(len(x)):
        z = np.dot(x[i], w)+b
        # z = sum(
        #     x[i][j] * w[j] 
        #     for j in range(len(w))
        # ) + b
        
        if z>0: 
            y_pred = 1
        else:
            y_pred = 0
            
        error = y_pred-y[i]
        w = w - alpha*error*x[i]
        b=b-alpha*error
        
    
print("Trained weights:", w)
print("Trained bias:", b)

for i in range(len(x)):
    z = np.dot(x[i], w)+b
    if z>0: 
        y_pred = 1
    else:
        y_pred = 0
        
    print(f"Input: {x[i]}, Predicted Output: {y_pred}")
            



