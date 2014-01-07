import math
import random
import time
import Tkinter
from scipy.spatial.distance import sqeuclidean
import numpy
#import matplotlib
#matplotlib.use('Agg')
#from scipy.cluster.vq import *
import matplotlib.pyplot as plt
import pylab
#pylab.close()


fp1=open("./ml-1m/users.dat","r")
user_desc={}
movie_desc={}
rating={}
for line in fp1.readlines():
    temp=line.split("::")
    user_desc[temp[0]]=[]
    rating[temp[0]]=[]
    if temp[1]=='F':
       user_desc[temp[0]].append(10)
    else:
       user_desc[temp[0]].append(20)
    user_desc[temp[0]].append(int(temp[2]))
    user_desc[temp[0]].append(int(temp[3]))
fp1.close()
#print user_desc

fp1=open("./ml-1m/movies.dat","r")
for line in fp1.readlines():
    temp=line.split("::")
    movie_desc[temp[0]]=[]
    movie_desc[temp[0]].append(temp[1])
    movie_desc[temp[0]].append([])
    temp1=temp[2].split("\n")
    temp1=temp1[0].split("|")
    for i in temp1:
        movie_desc[temp[0]][1].append(i)  
fp1.close()
#print movie_desc      

fp1=open("./ml-1m/ratings.dat","r")
for line in fp1.readlines():
    temp=line.split("::")
    rating[temp[0]].append([temp[1],temp[2]])
fp1.close()
#print rating

#defining the value of k, for the k-means
k=5
centroids=[]

i=0
index_bookeep=[]
while(i<k):
    index=random.randint(1,len(user_desc))
    if index in index_bookeep:
       continue
    else:
       centroids.append(user_desc[str(index-1)])
       index_bookeep.append(index)
       i=i+1

for kk in range(0,10):
  new_centroids=[]
  centroid_count=[]
  for i in range(0,k):
    new_centroids.append([0,0,0])
    centroid_count.append(0)

  point_centroid={}
  for i in range(0,len(user_desc)):
    smallest_dist=99999
    for j in range(0,len(centroids)):
        if sqeuclidean(user_desc[str(i+1)],centroids[j]) <= smallest_dist:
           smallest_dist=sqeuclidean(user_desc[str(i+1)],centroids[j])
           smallest_index=j
    point_centroid[str(i+1)]=smallest_index
    centroid_count[smallest_index]=centroid_count[smallest_index]+1

  #print centroid_count
  for i in range(0,len(user_desc)):
     for j in range(0,3):
           new_centroids[point_centroid[str(i+1)]][j] = new_centroids[point_centroid[str(i+1)]][j] + user_desc[str(i+1)][j]
  
  #print "new centroids", new_centroids
  for i in range(0,k):
    new_centroids[i]=map(lambda x: x/centroid_count[i], new_centroids[i])
  #print "centroids", centroids
  #print "new centroids", new_centroids
  #print "**************************************************"
  centroids=new_centroids
print centroids


gender=raw_input("what is ur gender :\n"
                     "if u are female type 10\n"
                     "If u r male, type 20\n"
                     "GENDER = ")
age=raw_input("how old r u : \n"  
        "*  1:  Under 18\n"
	"* 18:  18-24\n"
	"* 25:  25-34\n"
	"* 35:  35-44\n"
	"* 45:  45-49\n"
	"* 50:  50-55\n"
	"* 56:  56+\n"
               "AGE = ")
occupation=raw_input("waht is ur occupation\n"
          "0:  other or not specified\n"
	  "1:  academic/educator\n"
	  "2:  artist\n"
	  "3:  clerical/admin\n"
	  "4:  college/grad student\n"
	  "5:  customer service\n"
	  "6:  doctor/health care\n"
	  "7:  executive/managerial\n"
	  "8:  farmer\n"
	  "9:  homemaker\n"
	 "10:  K-12 student\n"
	 "11:  lawyer\n"
	 "12:  programmer\n"
	 "13:  retired\n"
	 "14:  sales/marketing\n"
	 "15:  scientist\n"
	 "16:  self-employed\n"
	 "17:  technician/engineer\n"
	 "18:  tradesman/craftsman\n"
	 "19:  unemployed\n"
	 "20:  writer\n"
               "OCCUPATION = ")
genre=raw_input("what kind of movie do you like : \n"
        "1: Action\n"
	"2: Adventure\n"
	"3: Animation\n"
	"4: Children's\n"
	"5: Comedy\n"
	"6: Crime\n"
	"7: Documentary\n"
	"8: Drama\n"
	"9: Fantasy\n"
	"10: Film-Noir\n"
	"11: Horror\n"
	"12: Musical\n"
	"13: Mystery\n"
	"14: Romance\n"
	"15: Sci-Fi\n"
	"16: Thriller\n"
	"17: War\n"
	"18: Western\n"
        "GENRE = ")
genre_list={}
genre_list[1]="Action"
genre_list[2]="Adventure"
genre_list[3]="Animation"
genre_list[4]="Children's"
genre_list[5]="Comedy"
genre_list[6]="Crime"
genre_list[7]="Documentary"
genre_list[8]="Drama"
genre_list[9]="Fantasy"
genre_list[10]="Film-Noir"
genre_list[11]="Horror"
genre_list[12]="Musical"
genre_list[13]="Mystery"
genre_list[14]="Romance"
genre_list[15]="Sci-Fi"
genre_list[16]="Thriller"
genre_list[17]="War"
genre_list[18]="Western"

#print genre
#print centroids
#Defining the value of k in k-nearest neighbour
nearest_cluster_dist=99999
new_point=[gender,age,occupation]
for i in range(0,k):
     dist=0
     for j in range(0,3):
         dist=dist+ pow((float(new_point[j])-float(centroids[i][j])),2)
     if nearest_cluster_dist > dist:
         nearest_cluster_dist=dist
         nearest_cluster=i
#     print dist
#print nearest_cluster

cluster_point = [key for key, value in point_centroid.iteritems() if value==nearest_cluster]
#print len(cluster_point)

movie_list={}
closest_neighbour={}
for i in cluster_point:
     for j in rating[i]:
          if ((int(j[1]) >3)&(genre_list[int(genre)] in movie_desc[j[0]][1])):
              dist=0
              for k in range(0,3):
                  dist=dist+pow((float(new_point[k])-float(user_desc[i][k])),2)
              movie_list[dist]=movie_desc[j[0]][0]
              closest_neighbour[dist]=user_desc[i]
#print movie_list

knn=10
best_selection=movie_list.keys()
best_selection.sort()
max_limit=0
print "Here is a list of movie suggestions for you\n********************************\n"
for i in best_selection:
    print movie_list[i]
    max_limit=max_limit + 1
    if max_limit == knn:
       break

##******************GRAPHS***************************************
a=point_centroid.values()
#print type(a[0])
idx=numpy.array(point_centroid.values())
#print "idx", idx
res=numpy.array(centroids)
#print "res", res
b=user_desc.values()
xy=numpy.array(b)
print "xy", xy
print type(xy)
colors = ([('blue', 'green', 'yellow', 'gray', 'magenta')[i] for i in idx])
#plt.scatterplot(xy[:,1],xy[:,2])
pylab.ylabel('occupation')
pylab.xlabel('age')
pylab.scatter(xy[:,1],xy[:,2], c=colors, marker='D')
pylab.scatter(res[:,1],res[:,2], marker='o', s = 500, linewidths=2, c='none')
pylab.scatter(res[:,1],res[:,2], marker='x', s = 500, linewidths=2)
#plt.plot([1,2,3,4])
pylab.show()
plt.subplot(2,2,1)
plt.xlabel('age')
plt.hist(xy[:,1],7)
plt.subplot(2,2,2)
plt.xlabel('Occupation')
plt.hist(xy[:,2],21)
plt.subplot(2,2,3)
plt.xlabel('Gender')
plt.hist(xy[:,0],2)
plt.subplot(2,2,4)
plt.xlabel('point in each centroid')
plt.hist(point_centroid.values(),5)
plt.show()
pylab.scatter(xy[:,1],xy[:,2], c=colors, marker='D')
pylab.scatter(new_point[1],new_point[2], marker='o', s = 500, linewidths=2, c='none')
pylab.scatter(new_point[1],new_point[2], marker='x', s = 500, linewidths=2)   
max_limit=0

for i in best_selection:
    plt.plot((float(new_point[1]),float(new_point[2])),(float(closest_neighbour[i][1]),float(closest_neighbour[i][2])))
    if max_limit==knn:
       break

pylab.show()





































