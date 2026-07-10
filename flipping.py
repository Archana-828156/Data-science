import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("orginal matrix:")
print(A)
print("flip column:",np.fliplr(A))
print("flip row:",np.flipud(A))