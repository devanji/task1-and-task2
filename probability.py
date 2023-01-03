import random

child1 = '0'
child2 = '0'
child3 = '0'

fff = 0
fmm = 0
mfm = 0
mmf = 0

exceptions = 0

for i in range (1000):
    child1 = random.choice('MF')
    child2 = random.choice('MF')
    child3 = random.choice('MF')
    if (child1 == 'F' and child2 == 'F' and child3 == 'F'):
        print("FFF")
        fff += 1
    elif (child1 == 'F' and child2 == 'M' and child3 == 'M'):
        print("FMM")
        fmm += 1
    elif (child1 == 'M' and child2 == 'F' and child3 == 'M'):
        print("MFM")
        mfm += 1
    elif (child1 == 'M' and child2 == 'M' and child3 == 'F'):
        print("MMF")
        mmf += 1
    else:
       exceptions += 1
        
        
print("Total FFF:",fff)
print("Total FMM:",fmm)
print("Total MFM:",mfm)
print("Total MMF:",mmf)
print("Total Exceptions:",exceptions)
