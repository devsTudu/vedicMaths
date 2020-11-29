from multiplication import topowerof10 as tp10


def divideby50(num):
	temp = num*2
	reply = tp10(temp,-2)
	return reply
	
	
def divideby125(num):
	temp = num*8
	return tp10(temp,-3)
	
	
def divideby5(number): # Only for intigers
    try :
        number = int(number)
    except:
        input('Hey, this module is only for intigers')
        return
    string = str(number)
    result = 0
    for num in string:
        temp = int(num)*2
        if temp > 9:
            result += temp//10
        result = result*10 + temp%10
    return result


def balanceit(alist):
    result = 0 
    for num in alist:
        result += num//10
        result *= 10
        result += num%10
    return result
    
    
def divideby9(number): #it returns a quotient and remainder separately
    string = str(number)
    values = []
    cumilative_sum = 0 
    for num in string:
        cumilative_sum += int(num)
        values.append(cumilative_sum)
    if values[-1]>=9:
        v = values.pop()
        q = divideSmallInt(v,9)[0]
        values.append(v+q)
    ans = str(balanceit(values))
    rem = eval(ans[-1])
    quot = eval(ans[:-1])
    return quot,rem


def cutIntoSizeOf(number,size):
    lis = []
    n = number
    tens = tp10(1,size)
    while n > 0:
        new = n%tens
        lis.append(new)
        n//= tens
    return lis[::-1]
    
    
    
'''the below code series of 9 raises error'''

def divbySerOf9(number,lenofSeries):
    l = lenofSeries
    nines = int('9'*l)
    values = []
    cumilative_sum = 0 
    # calculations
    numbers = cutIntoSizeOf(number,l)
    for num in numbers:
        cumilative_sum += num
        values.append(cumilative_sum)
    if values[-1]>=nines:
        v = values.pop()
        q = divideSmallInt(v,nines)[0]

        values.append(v+q)
        
    ans = str(balanceit(values))
    rem = eval(ans[-(l)])
    quot = eval(ans[:-(l)])
    return quot,rem
    

def divideSmallInt(numdiv,div):
	if numdiv<0 :
		numdiv *=	-1
		if div<0:
			div *=	-1
			bol =	True
		else :
			bol =	False
	else:
		if div<0:
			div *=	-1
			bol =	False
		else:
			bol =	True
	i = divnum = 0
	while True:
		i += 1
		divnum += div
		if divnum > numdiv:
			i -= 1
			divnum -= div
			break
	if not bol:
		i *= -1
	extra = numdiv - divnum
	return i,extra

def divideInt(num,bynum):
    quo = rem = r = ''
    string = str(num)
    boln=	False
    if '-' in string:
    	string = string[1:]
    	boln =	True	
    for anumber in string:
        temp = r + anumber
        print(anumber)
        q , r = divideSmallInt(int(temp),bynum)
        quo = quo + str(q)
        print('dividing ',anumber,'with',bynum,end='gets')
        print(q,'reminder',r)
    if boln:
    	quo =	'-'+quo
    rem = str(r)
    return quo,rem
    
n = 6839
qnt,rem = divideby9(n)
print(qnt)
print(qnt+rem/9,n/9)
j = 123456789
k = 4
print(divbySerOf9(j,k))
print(j//k,j%(10**k-1))
