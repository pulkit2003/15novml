##Q 1 Installed Python 3.10.0
                                                                   ##Output
##Q 2
5**9                                                               ##1953125
3//2                                                               ##1
7//3                                                               ##2
7/3                                                                ##2.3333333333333335
6==6                                                               ##True
a=20
a+=30
print(a)                                                           ##50
a%=3
print(a)                                                           ##2
True * False                                                       ##0
True & False                                                       ##False
True and False                                                     ##False
((6>3) and (7<4) or (18==3)) and (9>3)                             ##False
True is False                                                      ##False
False in 'False'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
((True == False) or (False > True)) and (False <= True)            ##False

##Q 3
s1 ="Nice to have it"
s2 =" here"
s3=s1+s2
print(s3)                                                          ##"Nice to have it here"

##Q 4
a =[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a[3][1][2][0]                                                      ##'hello'       
 
##Q 5
a.insert(0,s1)
a.append(s2)
print(a)                                                           ##['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, ' here']

##Q 6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
for i in numbers:
    if i==237:
        break
    elif i%2==0:
        print(i)

##Q 7
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list_1.difference(color_list_2)                             ##{'White', 'Black'}

##Q 8
import string  
alphabet = set(string.ascii_lowercase)
  
def ispangram(string):
    return set(string.lower()) >= alphabet
      
# Driver code                                       
string=input('Enter Value :')
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")

##Q 9
n = int(input('Enter any number n: '))
print(n+int(str(n)+str(n))+int(str(n)+str(n)+str(n)))

##Q 10
s=input("Enter a string : ")
l=s.split("#")
x=l[0].split(' ')
y=l[1].split(' ')
print(x)
print(y)

##Q 11
l = input('Enter the list of words: ')
lst = l.split(',')
print(','.join(sorted(lst)))

##Q 12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
d1=d['Marks']
l=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==l):
        j=i
d2=d['Student']
print(d2[j])

##Q 13
a=input('Enter any sentence :')
c=0
lc=0
for i in a:
    if i.isnumeric():
        c=c+1
    elif i.isalpha():
        lc=lc+1   
print('Letters {}'.format(c))
print('Alphabets {}'.format(lc))

##Q 14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
s=input('Enter a Subject: ')
l1=d['Name']
l2=[]
l3=[]
l4=d['Ratings']
l5=[]
sub=d['Subject']
for i in range(len(sub)):
    if sub[i]==s:
        l2+=[sub[i]]
        l3+=[l1[i]]
        l5+=[l4[i]]
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)

    
