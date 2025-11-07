#
# print(12,10,11,"hello",True,0)
# a=12
# print(a)
# print(type(a))
# a="hello"
# print(a)
# print(type(a))
# a=True
# print(a)
# print(type(a))
# a=13
# b=12
# a,b=b,a
# print(a,b)
# a,b,c=13,2.5,'hi'
# print(a,b,c)
# a=b=c=d=14
# a="hi"
# print(a*2)
#
# a=1+2j
# print(type(a))

# print('A',end='')
# print('B',end='')
# print('C',end='')
# print()
# print('D')
#
# a,b,c,d=10,15,20,25
# print(a,b,c,d)
# print(a,b,c,d, sep=',')
# print(a,b,c,d, sep=':')
# print(a,b,c,d, sep='--')

# a=input("please enter a number : ")
# print(type(a))
# a=eval(input("please enter a number : "))
# print(type(a))
# b=eval(input("please enter a number : "))
# print(type(a))
# a,b=eval(input('please enter number 1 , number 2:'))
# print(a,b)
# a=str(input("please enter a number : "))
# print(type(a))
# a=float(input("please enter a number : "))
# print(type(a))

# z=50
# a='print(z+100)'
# print(a)
# eval(a)
# eval(a,{'z':100})
# a='[1,2,3]'
# print(type(a))
# b=eval(a)
# print(b,type(b))
# a=eval('1>2')
# print(a)

# s='hello'
# print(s[0])
# print(s[2])
# print(s[1:4])
# print(s[1:])
# print(s[:3])
# print(s[-1])
# print(s[:])
# print(len(s))
#
# text='hello world , hello pyhton'
# print(text.replace('hello','hi'))
#
# text='{0} is a {1}, and {name} is a {role}'
# formatted_text=text.format('Alice','student',name='bob',role='teacher')
# print(formatted_text)

# help("keywords")

# colors=['green','red','black','blue']
# print(colors[1:3])
# print(type(colors))
#
# my_list=[1,2,3,4,5,6,7,8]
# print(my_list[::-1])
#
# my_list=[1,'hi',3]
# print(my_list)

# my_list=['hi',[8,4,6],['a']]
# print(my_list)
# print(my_list[1])
# print(my_list[1][1])



# colors=['green','red','black','blue']
# colors[1]='white'
# print(colors)
# colors[2:]=['r','g','h','p']
# print(colors)
# colors.append('pink')
# print(colors+['yellow']*3)
# colors.insert(1,'Blue')
# print(colors)
# colors.remove('pink')
# print(colors)
# del colors[1:8]
# print(colors)
# del colors
# print(colors)
# print('blue' not in colors)
# print(colors.index('green'))
# print(colors.index('blue'))
# print(colors.index('white',2,4))



# Train 1
# matris = eval(input("enter 9 numbers: ").split(","))
# matris = eval(input("enter 9 numbers: "))
matris = [12,32,34,32,56,64,34,64,56]
# print(matris)

# mainMatris = [matris[:3],matris[3:6],matris[6:]] 
# print(mainMatris)

row1 = matris[:3]
row2 = matris[3:6]
row3 = matris[6:]


mainMatris = [row1,row2,row3]
# print(row1[0],row2[0],row3[0])
# print(mainMatris)


# print(row1)

# print(row1[0],row2[1],row3[2])

# print(row1[2],row2[1],row3[0])

matris2 = [12,32,34,54,56,64,74,92,91]
matris2.sort(reverse=True)
# print(matris2)


# col1 = [row1[0],row2[0],row3[0]]
# col2 = [row1[1],row2[1],row3[1]]
# col3 = [row1[2],row2[2],row3[2]]

# print(row1[1] == row2[0] and row1[2] == row3[0] and row2[2] == row3[1])

sumMatris = sum(mainMatris,[])
# print(sumMatris)

centerNum = sumMatris.__len__()/2
centerNum_Main = int(centerNum)
#row2[1]

# print(centerNum_Main)

sumMatris = sum(mainMatris,[])

center_Cnt = sumMatris.count(centerNum)
# print(center_Cnt)




#Train 2
# text =input("enter text:")

# print(text.strip("()"))

# print(text.title())

# print(text.find(""))

# print(text.upper())

# print(text.lower())

# print(text.replace("-" , "_"))

# print(text.count("l"))

# print(text.swapcase())

# print(text.startswith("("))

# print(text.split("-"))

# print(text.partition("-"))



# matris = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# i = 0
# j = 0

# while( i < n):

#   for j in range(4):
#     matris[0][j]
#     j = j + 1

#   for j in x:
#     matris[j][3]
#     j = j + 1

#   for j in x:
#     matris[3][j]

  
# i=0
# j=0

# # matris = [[0 for j in  range(4)]]  
# s = 0
# # matris = [[0 for i in  range(4)]] 
# matris = [[0 for j in range(4)] for i in range(4)] 

# for j in range(4):
#     matris[0][j] = s
#     s =s+ 1

# for i in range(1, 4):
#     matris[i][3] = s
#     s =s+ 1

# # for i in range(2, 4):
# #     matris[i][3] = num
# #     num += 1

# for j in range(2, -1, -1):
#     matris[3][j] = s
#     s =s+ 1

# for i in range(2, 0, -1):
#     matris[i][0] = s
#     s =s+ 1


# for j in range(1, 3):
#     matris[1][j] = s
#     s =s+ 1

# for i in range(2, 1, -1):
#     matris[i][2] = s
#     s =s+ 1

# matris[2][1] = s

# for x in matris:
#     print(x)


# statement

# action = 'shoot'
# score = 0

# if action == 'shoot':
#   print ("shoot kard")

# elif action == 'pass':
#   print("pass dad be mamad")

# elif action == 'goal':
#   print("goalllll!")
#   score += 1

# else: 
#   print("daghghan dari che gohi mikhori?")

# if score > 0:
#   print(f"barandeh shodim ba {score} goal")
# else:
#   print("bakhtim ke")


# price = eval(input("Enter shoping bag price: "))
# discount = 0
# totalPrice = 0

# if price > 50000:
#   discount = 20
#   totalPrice = price - (price * discount / 100)
#   print(f"pay with 20% discount: {totalPrice}")

# elif 20000 < price < 50000:
#   discount = 10
#   totalPrice = price - (price * discount / 100)
#   print(f"pay with 10% discount: {totalPrice}")

# elif price < 20000:
#   print(f"pay without discount: {price}")


# my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
# count = 0

# for _ in my_list:
#    if _ % 2 == 0:
#       count += 1
# print(f"even numbers: {count}")


# for _ in "sina beyki":
#   print(_)

# people = (('sina' , 18) , ('ali' , 22) , ('sara' , 33))

# for name , age in people:
#   print(f"{name} with {age} old")

# people = {
#   'jadi':(17,165), 'sina':(21,180) , 'asal':(30,180)
# }
# for data in people.values():
#   # print(people[x][0])
#     print(data)


# n = 5
# x = 10

# for z in range(n):
#   if x % 2 == 1:
#     x = (x*2) - 1
#   elif x % 2 == 0:
#     x = x / 2

# print(x)


# while True:
#   print("Hello")

# print("oh! fuel is very low")
# f = 12

# while f <= 80:
#   f+=1
# print(f"fuel is {f}")

# x = 50

# while x !=  1:
#   if x % 2 == 0:
#     x = x / 2
#   else:
#     x = (x * 3) + 1

#   print(x)

# for a in [1,2,3]:
#   if a == 2:
#     break
#   print(a)




# Method functions

# num =[12,18,14,13,16,17,20,15,16,12,11,10,9,14,9,14,15,13]

def say_hello(name, n):
  for i in range(n):
    print(f"Hello {name}")

# say_hello('sina',3)
# say_hello('sari',1)

def sum_of_two_cases(a , b):
  res = a + b
  return res

# print( sum_of_two_cases(12,12) )


def capi_words(name):
  name = name.upper()
  print(name)

# capi_words('sina beyki')

def whats_a(name, c):
  count = 0
  for char in name:
    if char == c:
      count = count + 1
  print(count)

# whats_a('sina baba shodeh' , 'b')

def print_times(name , n=2 ): # default n value
  for i in range(n):
    print(name)

# print_times('sina')
