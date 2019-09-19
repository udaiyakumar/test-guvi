Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
a=[3,5,[3,56],3,[3,7,'zen',4.6],'guvi',5,2,'pit']

print(len(a))

count=0

m=0

for i in a:

    if isinstance(i,list):

        count+=1

        if m < len(i):

            m=len(i)

            index=a.index(i)

print("number of sublist in the list :",count)

print("sub list with maximum length is :",a[index])

print("index of sublist with max length is :",index)

print("first element of the sub list with max length is :",a[index][0])
