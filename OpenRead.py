
class MyClass():
   
   def __init__(self , file):
       self.file = file
       
    
      
   def DataCollection(self):
      dataCoil=[]
      a=1   
      for i in self.file:
          if a==0:
             break     
          i = self.file.readline()
          if i =='ENTITIES\n':
             for j in self.file:
                 j = self.file.readline()
                 if j =='AcDbCircle\n':
                   #  dataCoil+=j
                     for k in self.file:
                         k = self.file.readline()
                         if k =='ENDSEC\n':                             
                              break  
                         elif k == 'CIRCLE\n':
                              break   
                        # dataCoil+=k                  
                         dataCoil.append(k)
                 elif j =='ENDSEC\n':
                         a=0  # выход из условия
                         break   
                      
             
      return  dataCoil        
    
      
   def Scanner(self):
     
     returnList=[]
     k=-1
     dataColl=self.DataCollection()      
     for i in dataColl:
         returnList.append(float(i))

     dataColl.clear()
     for i in returnList:
        k+=1
        if k ==2:         
         localChar=i   
        else:
         dataColl.append(round(i,2))
         if k==3:
             k=-1

         
     return dataColl 
   