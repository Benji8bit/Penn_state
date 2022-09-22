def test() : # do not change this line!
 list = [4, 5, 1, 9, -2, 0, 3, -5] # do not change this line!
 min1 = list[0]
 min2 = list[1]
 # write your code here so that it sets
 # min1 and min2 to the two smallest numbers
 # be sure to indent your code!

 for i in range(len(list)):
     if list[i]<min1:
         if min1<min2:
             min2=list[i]
         else:
             min1=list[i]
     elif list[i]<min2:
         list[i]=min2

 print(min1, min2)
 return (min1, min2) # do not change this line!
# do not write any code below here
test() # do not change this line!
# do not remove this line!