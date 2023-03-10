
import matplotlib.pyplot as plt
import numpy as np
class var():
  x=[[1,1],[1,1.5],[1,2.5],[1,2],[2,1],[2,2]]
  y=[1,1,2,2,1,2]
  Rearranged_x=[]
  Rearranged_y=[]
  x1=[]
  x2=[]
  splitArr=[]




def scatter():
  #scatter is importent to know will we use x1 or x2 to differantiate between classes
  #plt.scatter(var.x2,var.y)
  #plt.scatter(var.x1,var.y)
  #plt.show()
  #if you want Active it delete the comment
  return 0




def ReArrangeClass1():

  for GetIndexForClass1 in range(0,len(var.x)):
    if var.y[GetIndexForClass1]==1:
      
      var.Rearranged_x.append(var.x[GetIndexForClass1])
      var.Rearranged_y.append(var.y[GetIndexForClass1])




def ReArrangeClass1Step2():
  return np.sort(var.Rearranged_x)





def ReArrangeClass2():
  targeted=[]
  
  for GetIndexForClass2 in range(0,len(var.x)):

    
    if var.y[GetIndexForClass2]==2:
      
      var.Rearranged_y.append(var.y[GetIndexForClass2])
      if len(targeted)==0:
        targeted.append(var.x[GetIndexForClass2])
        

      if len(targeted)>0:
        for loop in range(0,len(targeted)):
          if targeted[loop] > var.x[GetIndexForClass2]:

            targeted.insert(loop,var.x[GetIndexForClass2])
            
          if targeted[loop] < var.x[GetIndexForClass2]:

            targeted.insert(loop+1,var.x[GetIndexForClass2])
            

  for add in range(0,len(targeted)):
      var.Rearranged_x.append(targeted[add])
      






def IsolateX1andX2():
  for itr in range(0,len(var.x)):
    var.x1.append(var.Rearranged_x[itr][0])
    var.x2.append(var.Rearranged_x[itr][1])
    

def probabilityClass1():  
  p=var.splitArr.count(1)/len(var.splitArr)
  return p



  
 
def probabilityClass2(): 

  p=var.splitArr.count(2)/len(var.splitArr)
  return p





def GenrateSplitArrayItems(LastItrNo):
  for itr in range(0,len(var.y)):
    if LastItrNo>itr:
      var.splitArr.append(1)
    else:
      var.splitArr.append(2)




def GetTrgetedValue():
  CountValueEqual1=var.splitArr.count(1)
  
  
  return CountValueEqual1




def SplitByX2():
  for splitCount in range(0,len(var.y)):

    GenrateSplitArrayItems(LastItrNo=splitCount+1)
    GiniIndexInfo=GiniIndex()
    if GiniIndexInfo==.5 :

      targetedValue=GetTrgetedValue()
      print(targetedValue)

      return [var.x1[targetedValue],var.x2[targetedValue]]
    else:
     
      var.splitArr.clear()




  
  return 0
  


def GiniIndex():
  gini= (probabilityClass1()*(1-probabilityClass1()))+(probabilityClass2()*(1-probabilityClass2()))
  return gini
  

def MakeLine(ArrOfLine):
  x=ArrOfLine[0]
  y=ArrOfLine[1]
  return [x,y] 


def Predict(x_pred,y_pred):

  ReArrangeClass1()
  ReArrangeClass1Step2()
  ReArrangeClass2()
  IsolateX1andX2()
  ArrOfLineiNFO=SplitByX2()

  if MakeLine(ArrOfLineiNFO)[1]>y_pred:
    print("class1")

  if MakeLine(ArrOfLineiNFO)[1]<y_pred:
    print("class2")
  






if __name__=="__main__":
  Predict(x_pred=5,y_pred=5)



 ################################Documentation####################################
#this method called CART(CLASSIFICATION AND REGRESSION TREE) 
#this based on rearrange the points(important) 
#> get the point that separate the Points by calculate GINI 
#> use this point as line and sparate between classes 
#also its importent if ther is x1,x2,y in your database to plot them and understand what kind of parameter you will use to separate the points 
# in our case its x2 (which is in y axis)
