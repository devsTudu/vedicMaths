#importing neighbour modules
from Vedicmathscode1 import addall,substractAll



def genMultiplicationtable():
    table = {}
    for i in range(1,10):
        for j in range(1,10):
            table[(i,j)]= i*j 
    return table


def balanceit(alist):
    result = 0 
    for num in alist:
        result += num//10
        result *= 10
        result += num%10
    return result
    

mtable = genMultiplicationtable()


def multiplyint(ab,cd):
    #CHECKING signs of the number
    samesign= True
    if ab<0:
        ab *= -1
        if cd <0:
            cd *= -1
        else:
            samesign = False
    else:
        if cd<0:
            cd *= -1
            samesign = False
    # calculation part
    digitcounter = totalresult = 0
    while not ab==0:
        a,b = ab//10,ab%10
        tempresult = multiplyit(cd,b)
        tempresult = int(str(tempresult)+'0'*digitcounter)
        totalresult = totalresult+tempresult # change it in the actual program code 
        digitcounter += 1 
        ab = a
    if samesign:
        return totalresult
    else:
        return int('-'+str(totalresult))
        
    
    
def popnumat(num,position):
    string = str(num)+'0'
    try:
        val = int(string[position-1])
    except:
        val = 0
    return val
    
    
def multby11(num):
    lis = []
    l = len(str(num))
    for i in range(l+1):
        sum = popnumat(num,i)+popnumat(num,i+1)
        lis.append(sum)
    reply = balanceit(lis)
    return reply
    
    
    
def multiplyit(ab,x,carry=0,endstring=''):
    if ab == 0:
        return int(str(carry)+endstring)
    else:
        a,b = ab//10 ,ab%10
        result= mtable[(b,x)]+carry
        if result>=10:
            endstring = str(result%10)+endstring
            carry = result//10
        else :
            carry = 0 
            endstring = str(result)+endstring
        return multiplyit(a,x,carry,endstring)
        


        

def multby5(number):
    temp = str(number*10)
    reply = ''
    carry = 0
    for i in temp:
        if i in ('-','.'):
            reply = reply+i
            pass
        else:
            n = int(i)+10*carry
            reply = reply + str(n//2)
            if n%2== 0:
                carry = 0 
            else:
                carry = 1 
    reply = eval(reply)
    return reply


def multby125(number):
    print(notyet)
    return number*125

def notyet():
    print('not the the programme yet')

def multwithTensplaceSame(num1,num2):
    print("not created yet")
    return(num1*num2)
def basetechniwque(num1,num2):
    notyet()
    return num1*num2
def subbasetechnique(num1,num2):
    notyet()
def topowerof10(num, power):
    string = str(num)
    try :
        n = string.index('.')
        string = string.replace('.','')
    except:
        n = len(string)
    newposn = n+ power
    l = len(string)
    if l > newposn:
        if newposn>= 0:
            reply = string[:newposn]+'.'+string[newposn:]
        else:
            reply = '0.'+'0'*(-1*newposn)+string
    elif newposn==string:
        reply = string
    else:
        reply = string + '0'*(newposn-l)
    return eval (reply)
    
    
def multwithinteens(teen1,teen2):
    teen = (12,13,14,15,16,17,18,19)
    try:
        t1,t2 = int(teen1),int(teen2)
    except:
        print ('only integers are supported')
        return 
    if t1 in teen and t2 in teen:
        temp1 = t1+t2%10
        temp2 = (t1%10) * (t2%10)
        temp1 += temp2//10
        reply = topowerof10(temp1,1)+temp2%10
        return reply
    else :
        print (' Value must lie between 11 to 19')
        
 
def multbyEqualDigitsof9(number):
    string = str(number)
    reply = string[:-1]
    lastdigit = int(string[-1])
    if lastdigit == 0:
        reply = str(substractAll(reply,1)) + '9'
    else :
        reply = reply + substractAll(lastdigit,1)
    for i in range(len(string)-1):
        reply = reply + str(9-int(string[i]))
    reply = reply + str(10-int(string[-1]))
    return reply

     
def multbySeriesof9(number,lengthofseries):
    string = str(number)
    if lengthofseries == len(string):
        return multbyEqualDigitsof9(number)
    else:
        reply = int(string+'0'*lengthofseries)
        reply = substractAll(reply,number)
        return reply
        


def multwithteen(number,teen):
    if teen not in range(12,20):
    	print('the second value must be  between 12 to 19')
    	return 
    try:
        int(number)
    except:
        print ('Only integers allowed')
        return
    string = '0'+str(number)
    l = len(string)
    n = teen%10
    lis = []
    for i in range(l):
        val = int(string[i])*n
        if i == (l-1):
            pass
        else:
            val += int(string[i+1])
        lis.append(val)
    reply =  balanceit(lis)
    return reply
    
    
def mult2digswithonesplace1(num,n1):
    if (n1//100==0) and (n1%10==1):
        n = n1//10
        lis = []
        l = len(str(num))
        for i in range(l+1):
            sum = n*popnumat(num,i+1)+popnumat(num,i)
            lis.append(sum)
        reply = balanceit(lis)
        return reply
        
def by_factors(num1,num2):
    print('Not yet created')
    return num1*num2

def vilokanamtechnique():
    return
    
        
while 1:
	a =int(input('Number please:'))
	b =int(input('ones place 1 :'))
	print('to product it gives:',mult2digswithonesplace1(a,b))
	print('In classical way   :',b*a)
