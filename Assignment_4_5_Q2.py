def test() : # do not change this or the next line!
  numbers = [11.5, 28.3, 23.5, -4.8, 15.9, -63.1, 79.4, 80.0, 0, 67.4, -11.9, 32.6]
  average = 0

  # write your code here so that it sets average
  # to the average of the non-negative numbers
  # be sure to indent your code!
  sum = 0
  count = 0
  for i in range(len(numbers)):
      if numbers[i]>=0:
          sum += numbers[i]
          count+=1
  average = sum/count

  print(average)
  return average # do not change this line!
  # do not write any code below here

test()  # do not change this line!
# do not remove this line!
