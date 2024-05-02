#import string


#a = 4.5
#b = 2
#print(a // b)

#test_str = 'Learning Automation: for ! RD;'
#test_str = test_str.translate
#(str.translate('','',string.punctuation))
#print(test_str)


#def fibonaci():
#    a, b = 0, 1
#    while True:
#        yield a
#        a, b = b, a + b


#f1 = fibonaci()
#for i in f1:
#    print(i)


list1 = [41, 2, 12, 6, 35, 8, 10, 1, 19]
n = len(list1)

for i in range(n):
    for j in range(i + 1, n):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)



#avg = lamda x,y:(x+y)/2

def say_hello():
    return"Hello world"






