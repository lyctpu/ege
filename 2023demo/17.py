with open('17.txt') as f:
   numbers=[int(x) for x in f]
   print(numbers)
   s=[]
   for i in range(1,len(numbers)):
      if numbers[i]%3==0 or numbers[i-1]%3==0:
         s.append(numbers[i]+numbers[i-1])
   print(len(s), max(s))