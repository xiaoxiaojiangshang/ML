import numpy as np
a=np.random.rand(4,4)
randMat=np.mat(a)
b=randMat.I
invRandMat=b.I
c=a*b
d=np.eye(4)
print(c-d);

