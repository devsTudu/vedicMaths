# backend codes

def makeofEqualsize(num1,num2,mixed=True): # if 23.2 and 4.12 are given it returns 23.20 and 04.12 in string format
    d1 = str(float(num1)).split('.')[1]
    d2 = str(float(num2)).split('.')[1]
    while len(d1)!=len(d2):
        if len(d1)>len(d2):
            d2= d2+'0'
        else:
            d1 = d1+'0'
    i1 = str(float(num1)).split('.')[0]
    i2 = str(float(num2)).split('.')[0]
    signofn1 = ''
    if '-' in i1:           #taking the signs out so that they dont afect the length
        signofn1 = '-'
        i1.replace('-','')
    signofn2 = ''
    if '-' in i2:
        signofn2 = '-'
        i2.replace('-','')
    
    while len(i1)!=len(i2):
        if len(i1)>len(i2):
            i2= '0'+i2
        else:
            i1 ='0'+ i1
    i1 = signofn1+i1.replace('-','')
    i2 = signofn2+i2.replace('-','')
    number1 = i1+'.'+d1
    number2 = i2+'.'+d2
    if mixed:
        return number1,number2
    else:
        return i1,d1,i2,d2



def balanceit(alist):
    result = 0 
    for num in alist:
        result += num//10
        result *= 10
        result += num%10
    return result
    

def genAddtable():
        table = {}
        for i in range(10):
            for j in range(10):
                table[(i,j)] = i+j 
        return table

def genSubtable():
    table = {}
    for i in range(11):
        for j in range(10):
            table[(i,j)]=i-j
    return table


def value(number):
    try:
        reply = int(number)
    except:
        reply = float(number)
    else:
        reply = number
    return reply


def compareBoth(num1,num2):
    a,b = str(num1), str(num2)
    if a == b :
        return 'equal'
    elif '-' in a and '-' not in b:
        return 'smaller'
    elif '-' not in a and '-' in b:
        return 'greater'
    else:
        eA,eB = makeofEqualsize(num1,num2)
        for i in range(len(eA)):
            if eA[i]==eB[i]:
                continue
            else:
                n1 = int(eA[i])
                n2 = int(eB[i])
                if '-' in eA:
                    if n1 > n2:
                        return 'smaller'
                    else:
                        return 'greater'
                else:
                    if n1 > n2:
                        return 'greater'
                    else:
                        return 'smaller'

removeDecimalpoint = lambda num : int(num.replace('.',''))
changeNegativeToPositiveInteger = lambda num : int(str(num)[1:])

# some generic table and values
        
aTable = genAddtable()
sTable = genSubtable()



# real calculations definations below
def substractInt(ab,cd, credit= 0, endstring='',proper=True):
    if isinstance(ab,float) or isinstance(cd,float):
        return substractAll(ab,cd)
    ab = int(ab)
    cd = int(cd)
    if proper and ab<cd:
        proper = False
        ab,cd = cd,ab #swapping values
    if cd == 0:
        if credit!=0 :
            ab -= credit
        else:
            pass
        temp = str(ab)
        if proper:
            temp = temp + endstring
        else: 
            temp = '-'+endstring
        return value(temp)
    a,b = ab//10,ab%10
    c,d = cd//10,cd%10
    b = b - credit
    if b<d:
         credit= 1
         temp = b + sTable[10,d] # compliment of d
    else:
         credit = 0 
         temp = sTable[b,d]
    endstring = str(temp)+endstring
    return substractInt(a,c,credit,endstring,proper)


def substractAll(num1,num2):    # needs little repair 
    if num1<0 and num2<0:
        resultWillbeNegative = True
        num1,num2 = changeNegativeToPositiveInteger(num1),changeNegativeToPositiveInteger(num2)
    else:
        if num1<0 and num2>0:
            reply = '-'+str(addall(changeNegativeToPositiveInteger(num1),num2))
            return reply
        elif num2<0 and num1>0:
            reply = addall(num1,changeNegativeToPositiveInteger(num2))
            return reply
        resultWillbeNegative = False

    if num2>num1: # get a vedic math style ie isBigger(num,from)
        num1, num2 = num2,num1
        resultWillbeNegative = True
    else :
        resultWillbeNegative = False
    n1,n2= makeofEqualsize(num1,num2,True)
    try:
        ind = substractInt(len(n1), n1.index('.')) - 1
        ind *= -1
    except :
        ind = 'n'
    n1 = removeDecimalpoint(n1)
    n2 = removeDecimalpoint(n2)
    result = str(substractInt(n1,n2))
    while len(str(n1))>len(result):
        result = '0'+result
    if ind != 'n':
        result = result[:ind]+'.'+result[ind:]
    if resultWillbeNegative:
        result = '-'+ result
    result = result[1:-1].lstrip('0')    #it returned two zeros extra, in sufix and prefix if not sliced
    reply = value(result)
    return reply

def substractiondoubledigit(num1,num2):
    print ('Yet not programmed')
    return num1-num2

def substractTripleDigit(x,num1):  #in format 10^x-num1
    print("yet not coded")
    return(10**x-num1)
    

def add(num1,num2,carry= 0,endstring='',signofResult=''):
    if isinstance(num1,float) or isinstance(num2,float):
        return addall(num1,num2)
    else:
        if (num1<0 and num2<0 ):
            signofResult = '-'
            num1 = changeNegativeToPositiveInteger(num1)
            num2 = changeNegativeToPositiveInteger(num2)
        if num1<10 and num2<10:
            temp = aTable[(num1,num2)]
            temp = carry + temp
            temp = int(str(temp)+endstring)
            return temp
        else:
            if num1>9:
                s1 = num1%10
                num1 = num1//10
            else :
                s1 = num1
                num1 = 0
            if num2 > 9:
                s2 = num2%10
                num2= num2//10
            else:
                s2 = num2
                num2=0
            temp = aTable[(s1,s2)]
            temp = temp + carry
            if temp>9:
                carry = temp//10
                temp= temp%10
            else :
                carry = 0 
            while '-' in endstring:
                point = endstring.index('-')
                endstring = endstring[:point]+endstring[point+1:]
            endstring =signofResult+ str(temp)+endstring
            return(add(num1,num2,carry,endstring))
            
            
def addall(num1,num2):
    i1,d1,i2,d2 = makeofEqualsize(num1,num2,False)
    sum_i = add(int(i1),int(i2))
    sum_d = add(int(d1),int(d2))
    sum_d = str(sum_d)
    if len(sum_d)>len(d1):
        sum_i = add(int(sum_d[0]),sum_i)
        sum_d = sum_d[1:]
    while not(len(sum_d)==len(d1)):
        sum_d = '0'+ sum_d
    
    mixing = str(sum_i) + '.'+sum_d
    return value(mixing)


def addseries(*number):
    total = 0
    for i in number:
        total = addall(total,i)
    return value(total)


    
def divideby9(number):
    string = str(number)
    values = []
    cumilative_sum = 0 
    for num in string:
        cumilative_sum += int(num)
        values.append(cumilative_sum)
    if values[-1]>=9:
        values.append(values.pop()+1)
    result = balanceit(values)/10
    return result

def main():
    print(addseries(14.8,15.9,56.6,234,53.6))
    print()
    #a = float(input("Enter a number:"))
    #b =  float(input("Enter the second number:"))
    lis = (345,-56.45,-56.2,3.56,-55.5,4.44,44.4,-35.6,35.61)
    try:
        for i in range(len(lis)):
            a,b = lis[i],lis[i+1]
            print(a,compareBoth(a,b),b)
    except:
        pass


def test():
    a = float(input("Enter a number"))
    b = float(input("Enter another number"))
    print(makeofEqualsize(a,b))




while 1:
    test()
