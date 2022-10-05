with open('24.txt') as f:
   letters=f.readline()
   count,maximum=0,0
   text=''
   delta=0
   for i in range(0,len(letters)-1):

      if (letters[i]=='C' or letters[i]=='D' or letters[i]=='F') and (letters[i+1]=='A' or letters[i+1]=='O'):
         delta=0
         text=text+letters[i]+letters[i+1]
         count+=1
         if count>maximum: 
            maximum=count
     
      else: delta+=1
      if delta==2:
         count=0
         text=''
print(maximum)
