def fizzbuzz(list1,list2):
    total=0
    total=sum(list1)+sum(list2)
    
    if total%3==0:
       return "fizz"
    elif total%5==0:
          return "buzz"
    else:
        return total
  
print(fizzbuzz(([1,2,3,4]),(5,6,7,8,4)))
