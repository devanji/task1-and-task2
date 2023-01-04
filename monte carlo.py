import random

def random_A():
    return random.randint(8,12)

def random_B():
    return random.randint(10,14)

def random_C():
    return random.randint(12,16)

T1 = 0
T2 = 0
T3 = 0

for i in range(500):
  Activity_A = random_A()
  Activity_B = random_B()
  Activity_C = random_C()
  
  SUM = Activity_A + Activity_B + Activity_C
  
  if SUM >= 30 and SUM <= 35:
      T1+=1
  if SUM >= 36 and SUM <= 38:
      T2+=1
  if SUM >= 39 and SUM <= 42:
      T3+=1
      
probability1 = T1/500
probability2 = T2/500
probability3 = T3/500
  
print(probability1, probability2, probability3)
