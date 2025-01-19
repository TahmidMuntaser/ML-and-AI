import numpy as np
import matplotlib.pyplot as plt


x = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y = np.array([0, 0, 0, 1])

w = np.array([0, 0])
# w = [0,0]
b = 0
alpha = 0.1

# training

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
        

# Test
        
print("Trained weights:", w)
print("Trained bias:", b)

for i in range(len(x)):
    z = np.dot(x[i], w)+b
    if z>0: 
        y_pred = 1
    else:
        y_pred = 0
        
    print(f"Input: {x[i]}, Predicted Output: {y_pred}")
            





plt.figure(figsize=(8, 6))

# Plot data points
for i in range(len(x)):
    if y[i] == 0:
        plt.scatter(x[i][0], x[i][1], color='red', marker='o')
    else:
        plt.scatter(x[i][0], x[i][1], color='blue', marker='x')

# Plot decision boundary
x1 = np.linspace(-0.5, 1.5, 100)
x2 = -(w[0] * x1 + b) / w[1]
plt.plot(x1, x2, color='green', linestyle='--')

plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Perceptron Decision Boundary for AND Gate')
plt.grid(True)
plt.show()