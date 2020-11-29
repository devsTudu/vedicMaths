import Vedicmathscode1 as vd 
import random as rd

#checking simple additions and substractions

print('Checking all the additions NOW..')
ctr = 0
for i in range(1000):
    n1 = rd.randint(-1200,1000)
    n2 = rd.randint(-1245,5356)
    classical = float(n1+n2)
    try:
        vedic = vd.addall(n1,n2)
    except:
        print(i,n1,n2)
        input('Gives error')
        continue
    if classical==vedic:
        pass
    else:
        print('error in calculation:',i,n1,n2,classical,vedic)
        input('Proceed aheaed')