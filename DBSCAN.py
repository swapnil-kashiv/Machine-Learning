import pandas as pd
import random as rd
import numpy as np

class algo:

  def __init__(self,pts,minPts,eps):
    self.pts=pts
    self.minPts=minPts
    self.eps=eps

  def neighbourhood(self,p): 
    nb=[]
    for po in self.pts.itertuples(index=True,name=None):
      if po not in visited:
        dstnce=np.sqrt((p[1]-po[1])**2 + (p[2]-po[2])**2)
        if dstnce<=self.eps:
          nb.append(po)
          visited.append(po)
    return nb 

  def Cluster(self,pt,nb,clr):
    points["cluster"].iloc[pt[0]]=clr
  
    for p in nb:
      nbrhood=algo.neighbourhood(self,p)
      if len(nbrhood)>=self.minPts:
        algo.Cluster(self,p,nbrhood,clr)
      else:
        for x in nbrhood:
          points["cluster"].iloc[x[0]]=clr
        points["cluster"].iloc[p[0]]=clr
        return ""
      

  def DBSCAN(self):
    
    for p in self.pts.itertuples(index=True,name=None):
      if p not in visited:
        visited.append(p)
        nbhd=algo.neighbourhood(self,p)
        
        if len(nbhd)>=self.minPts:
          algo.Cluster(self,p,nbhd,p[0])
        else:
          for x in nbhd:
            if x[3]!='noise':
              visited.remove(x)
          points["cluster"].iloc[p[0]]="noise"


if __name__=="__main__":
 
  visited=[]
  i=0
  nbhd={}
  clstr={}
  points_1=pd.DataFrame({'x':[rd.randint(0,10) for x in range(50)],
  'y':[rd.randint(0,10) for x in range(50)],
  'cluster':""
  })
  #points_1.to_csv("test.csv")
  points=pd.read_csv("test.csv")
  points.drop(points.columns[0],axis=1,inplace=True)
  obj=algo(points,3,2)
  obj.DBSCAN()
  print(points)
