##value = 12
##
##while len(str(value)) == 2:
##    print(value)
##    value = str(value)
##    print(type(value)) # <class 'str'>
##    while len(value) == 2:
##        print(len(value)) # 2
##        value = str(value)
##        print(type(value)) # <class 'str'>
##        # value type is str
##        value1 = int(value[0])
##        print(type(value1)) # <class 'int'>
##        value2 = int(value[1])
##        print(type(value2)) # <class 'int'>
##        sum2 = value1 + value2
##        print(sum2) # 3
##        value = str(sum2)
##    
##    print("{} + {} = {}".format(value1, value2, sum2)) # 1 + 2 = 3
##
##print("DONE...") # DONE...

def luhn_test(cc_num):
    sum2 = 0
    #count = 0
    for digit in cc_num[-2::-2]:
        #count += 1
        #print("Count:", count)
        value = int(digit) * 2
        #print(value)
        value = str(value)
        if len(value) == 2:
            digit1 = int(value[0])
            #print(digit1)
            digit2 = int(value[1])
            #print(digit2)
            sum2 = int(digit1) + int(digit2)
            
        else:
            sum2 = value


    
luhn_test("4388576018402626")
