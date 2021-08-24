

a= [1,2,3,1]
def bubbleSort(a):
 count=1
 print(a ,end="-> original \n")
 for i in range(len(a)):
  for j in range(len(a)-i-1):
    if a[j]>a[j+1]:
     a[j],a[j+1]=a[j+1],a[j]  
     print(a ,end=" <-->")
     print(count) 
     count=count+1  
     
bubbleSort(a)     