def countvowels(string): 
  count=0
  for x in string:
    if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
     print(x) 

  for x in range(len(string)-1):
      for y in range(x+1, len(string)):
          if string[x]==string[y]:
              count+=1
  print(count)              
   
countvowels('drinkwater')
