from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq

fp=open("GHIJ-nooutliers","r")
kk=[]
for i in fp.readlines():
     temp0=i.split("::")
     temp1=[]

     if temp0[1]=="F":
        temp1.append(10)
     else:
        temp1.append(20)

     temp1.append(int(temp0[2]))
     temp1.append(int(temp0[3]))
     kk.append(temp1)

# data generation
data = vstack((kk))
print data

# computing K-Means with K = 2 (2 clusters)
centroids,_ = kmeans(data,2)

# assign each sample to a cluster
idx,_ = vq(data,centroids)
print idx,_

# some plotting using numpy's logical indexing
plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plot(centroids[:,1],centroids[:,2],'sg',markersize=8)
show()

