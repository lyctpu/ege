with open('17.txt') as f:
   numbers=[int(x) for x in f]
   print(numbers)
   maxi=[]
   s=[]
   
   for i in range(0,len(numbers)):
      if numbers[i]%10==3:
         maxi.append(numbers[i])
   maximum=0
   for i in range(len(numbers)-1):
      if ((abs(numbers[i])%10==3) and (abs(numbers[i+1])%10!=3)) or\
         ((abs(numbers[i])%10!=3) and (abs(numbers[i+1])%10==3)):
         if (numbers[i]**2+numbers[i+1]**2) >= max(maxi)**2: 
               s.append(numbers[i]+numbers[i+1])
               if numbers[i]**2+numbers[i+1]**2>maximum:
                  maximum=numbers[i]**2+numbers[i+1]**2
   print(len(s), maximum)
