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
# print('sina' , end = '***')

def tavan(n , t):
  
  javab = n
  for i in range(t):
    javab *= n
  return javab

# print(tavan(2,5))



def is_even(n):
  
  return n % 2 == 0

# print(is_even(43))


def num_of_even(nums):
  count = 0
  for n in nums:
    if is_even(n):
      count += 1
  any_even = count >= 1
  return any_even
    

# print( num_of_even([1,3,5,7]))


def largest(nums):
  largest_n = -1
  for i in nums:
    if largest_n < i:
      largest_n = i
  return largest_n

my_numbers = [1,2,3,6,12,8,63,22,54,255]
lg_number = largest(my_numbers)
# print(lg_number)


def num_of_odd(nums):
  count = 0
  gopsfand = []
  for khar in nums:
    if not is_even(khar):
      gopsfand.append(khar)
      count += 1
  return gopsfand , count

my_odd , odd_count = num_of_odd(my_numbers)
# print(my_odd , odd_count , sep=' | ')


def jam_zarb(a , b):
  jam = a + b
  zarb = a * b
  return jam , zarb

# print(jam_zarb(2 , 3))

donation = {
  'jadi': 20,
  'sara': 800,
  'zar' : 12,
  'hasan': 9
}

def user_donation(don):
  
  person = ''
  total = 0
  count = 0
  
  first_val = list(don.values()) [0]
  max_dona = first_val
  # print(max_dona)
  
  for name , value in don.items():
    total += value
    count += 1
    if value > max_dona:
      person = name
      max_dona = value
  average = total / count
  return average , total , person


avg, total, max_user = user_donation(donation)

# print(f"total donation: {total}")
# print(f"average donation: {avg}")
# print(f"thanks to {max_user}")

# end jadi


# start usb 

menu = {
  "breakfast": "cheese",
  "lunch2": "koobideh",
  "dinner":"gheymeh",
  "lunch": "joojeh"
}

# print(menu.items())

def menu_key(dict , key):
  
  for i in dict.keys():
    
    if i == key:
      return ( dict.get(key) )
    
menu_key(menu , "lunch2")


def f(a,b,c):
  return(f"a = {a} | b = {b} | c = {c}")
  
f(b=1,a=2,c=3)


my_list = [1,'hi',3]
f(*my_list)


b = {'a':1, 'b':2 , 'c':3}
f(**b)


my_list2 = [21,15,36,18,27]

def set_name():
  global scope
  scope = 'local'
  
set_name()
# print(scope)


def set_global_scope():
  global scope
  scope = 'global'
  
def set_scope():
  scope = 'local'
  
def printscope():
  print(scope)
  

scope = None
set_global_scope()
set_scope()
# printscope()


def f(a):
  a = a * a
  # print(a)
  
b = 3
f(b)
# print(b)

def f(a):
  a += ' world'
  # print(a)

b = 'hello'
f(b)
# print(b)


def f(a):
  a[0] = 3
  # print(a)
  
b = [1,2]
f(b)
# print(b)

# end usb


# start jadi 
def guess_game():
  import random
  
  computer_rendom = random.randint(1 , 20)
  guess = 0
  count = 0
  
  # print(computer_rendom)
  
  def welcome():
    print("welcome to this funny game")
    print("I will guess a number between 1 to 100")
    print("you have to guess it...")
    print("GO GO GO")
    print()
  
  def finish(number , count):
    print("Gg boy :)")
    print(f"my number was {number} and you founded it in {count} guesses!")

  def win(computer_rendom , guess):
    if computer_rendom == guess:
      return True
    else:
      return False

  def answer(computer_rendom , user):
  
    if computer_rendom > user:
      return 'my number is larger'
    elif computer_rendom < user:
      return 'ohh.. you went so large!mine is smaller'
    
    return 'wow! you won! good guess!'
  
  
  def get_a_guess():
    ans = input("what is your guess? ")
    return int(ans)

    
  while (not win(computer_rendom , guess)):
  
      guess = get_a_guess()
      count += 1
      print(answer(computer_rendom,guess))
  
  finish(computer_rendom , count)
  
# guess_game()
  
def hello_name(name):
  print(f"hello, {name}")
  
# hello_name('sina')

def is_postivie(number):
  
  if number >= 0:
    return True
  else:
    return False

# print(is_postivie(-9))


def sum_of_suares(n1 , n2):
  return n1**2 + n2**2

# print(sum_of_suares(3,4))

def is_even(numb):
  if numb % 2 == 0:
    return True
  else:
    return False

# print(is_even(6))


def is_greater(a,b):
  if a > b :
    return True
  else:
    return False
  
# print(is_greater(4,9))


def zarb(*args):
  res = 1
  for i in args:
    res *= i
  return res

# print(zarb(3,4,5,6,7,8))



def masahat(**kwargs):
  if 'tool' in kwargs:
    return kwargs['tool'] * kwargs['ertefa']
  if 'shoa' in kwargs:
    return kwargs['shoa'] * 3.14 * kwargs['shoa']
  return 100
  

# print(masahat(shoa=8))




def pick_evens(*args) :
  evens = []
  for i in args:
    if i % 2 == 0:
      evens.append(i)
  return evens

# print(pick_evens(2,3,13,45,67))


def skyline(*args):
  max_sky = 0
  for i in args:
    if i > max_sky:
      max_sky = i
  return max_sky

# print(skyline(230,440,456,900,1290,1234,4312,1243,5467,1243,3212,4312,2345))




# Train Two

# def main():
  
#   while 1:
#     print("Welcome to Twitter Company")
#     print('1- Add User')
#     print('2- Search by id')
#     print('3- edit usrt')
#     print('4- delete user')
#     print('5- salary checker')
#     print('6- Total Salary')
#     print('7- Filter and sort data')
#     print('8- undo removes')
    
#   x = eval(input("enter your choise: "))
  
#   if x == 1:
#     add_user()
    
#   elif x == 2:
#     show_user()
    
#   def load_data():
    
#     perso_data = 'perso_data.txt'
#     userDic = {}
#     trash = []
    
#     with open(perso_data, 'r', encoding='utf-8') as file:
#       for i in perso_data:
#         data = i.strip().split()
        
      
  
#   def add_user():
    
#     while 1:
      
#       user_id = eval(input("Enter user id: "))
      
#       if user_id == -1:
#         print("exit... your information was saved.")
#         break
        
#       user_name = input("Enter user name: ")
#       user_totalTime = eval(input("Enter user Total Time of Work: "))
#       user_HourCash = eval(input("Enter user Cash per hour works: "))
      
#       userDic[user_id] = {
#         "id" : user_id,
#         "name" : user_name,
#         "total_Time" : user_totalTime,
#         "hour_cash" : user_HourCash
#       }
      
#       FileFormat = f"ID: {user_id} | Name: {user_name} | Total time works: {user_totalTime} | Cash per hours : {user_HourCash}\n"
      
#       with open (perso_data , 'a' , encoding='utf_8') as file:
#         file.write(FileFormat)
  
#   def show_user():
  
#     search_id = eval(input("Enter id to search: "))
    
#     for search_id in userDic:
#       target_data = userDic[search_id]
      
#       print (f"name : {target_data["name"]} |")
      
#     else:
#       print("user not found !!!!")
  

# main()

class personal:
  def __init__(self, name , grade , color):
    self.name = 'sina',
    self.grade = 12,
    self.color = 'black'
    
    
    
# ی متد بازشگتی بنویسید که تعداد کلمات داخل یک رشته برگردونه و قبلش رشته رو معکوس کنه
# ابع بازگشتی که تعداد کلمات و برگدونه


    
# def reverb_str(string):
#   text = 


# def revers(name):
#   if len(name) == 0:
#     return False
  
#   else:
#     return revers(name[1:]) + name[0]
   

# print(revers('emad'))

def count_harf(name):
  
  count = 0
  # name = name.strip()
  
  if name == "":
    return 0
  
  if name == " ":
    return 1
  
  # name_sp =name.find(" ")
  
  n = name.len()
  
  for i in n:
    if i == " ":
      count += 1
      
  
  return count_harf 
  
# print(count_harf("emad alww"))


#jadi oop

class ClassName():
  def __init__(self , name):
    self.name= name
    # print(f"created user: {self.name}")
  def say_hello(self):
    print(f"hello {self.name}")
    
s = ClassName('sina')

# s.say_hello()

class circle():
  pi = 3.1415926
  def __init__(self , r):
    self.r = r
    
  def masahat(self):
    return self.r * self.r * self.pi


c1 = circle(10)


# print(c1.masahat())


class book():
  booktype = 'horror'
  def __init__(self , name , page):
    self.name = name
    self.pages = page
    
    
  def open(self):
    print(f'opened the {self.name} which has {self.pages} pages')

class darsi(book):
  def __init__(self, reshteh , paye , name , page):
    book.__init__(self , name , page)
    # print('a new darsi book')
    self.reshteh = reshteh
    self.paye = paye
    
  def open(self):
    print(f'opened the {self.name} which has {self.pages} pages in the {self.reshteh} reshteh and in paye {self.paye}')
    
d = darsi('riazi' , 3 , '300 noskhe' , 120)
# print(d.open())



#abstract oop
class Human():
  def __init__(self , name):
    pass
  
  def jump(self):
    raise NotImplementedError("ImplementJump Error")
  
class Programmer(Human):
  
  pass

  def jump(self):
    print("I Jumped ...")
  
Sina = Programmer("Sina")
# print(Sina.jump())

 





