total=0
while True:
  Iprice=int(input("if 0 break"))
  if Iprice>=10000:
    Iprice*=0.9
  total+=Iprice
  if Iprice==0:
    break
print(total)