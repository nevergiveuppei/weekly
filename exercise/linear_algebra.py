
#test
#creat a random matrix a
#import numpy     
#ii = numpy.random.randn(2, 3) 
#print(ii)
#print(ii.T)
#end test

#inverse matrix
import numpy as np
aa=np.array(([1.,2.],[3.,4.])) 
print(aa)
#aai=np.linalg.inv(aa)
#print(aai)
#print(np.dot(aa,aai))

#bb=np.array(([1,1,1],[0,2,5],[2,5,-1]))
#bbi=np.linalg.inv(bb)
#print(np.dot(bb,bbi))

#determinant
#aa_det=np.linalg.det(aa)
#print(aa_det)

#eigenvalues & eigenvectors
print("eigenvalues ",np.linalg.eigvals(aa))
eigenvalues, eigenvectors = np.linalg.eig(aa) 
print("eigenvectors :\n", eigenvectors)

#bb = np.dot( np.linalg.inv(eigenvectors), np.dot(np.array([eigenvalues[0], 0.],[0.,eigenvalues[0]]), eigenvectors))
#bb = np.dot(np.array([eigenvalues[0], 0.],[0.,eigenvalues[0]]), eigenvectors)
bb = np.array(([eigenvalues[0], 0.],[0.,eigenvalues[1]]))
bb = np.dot(bb, np.linalg.inv(eigenvectors),)
bb = np.dot(eigenvectors, bb)
print(bb)



