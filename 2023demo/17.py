with open('17.txt') as f:
   numbers=[int(x) for x in f]
   print(numbers)
   maxi=0
   s=[]
   
   for i in range(0,len(numbers)):
      if numbers[i]%10==3:
         maxi.append(numbers[i])
   
   for i in range(1,len(numbers)):
      if (numbers[i]%10==3) ^ (numbers[i-1]%10==3):
         if (numbers[i]**2+numbers[i-1]**2) >= max(maxi)**2: 
            s.append(numbers[i]+numbers[i-1])
   print(len(s), max(s))