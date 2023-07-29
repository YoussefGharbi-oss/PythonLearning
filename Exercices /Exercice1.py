#Exxercice1 : Reverse a tuple
my_tuple = (10, 12, "Mark", "12.5")
#slice the tuple with empty start and empty end and -1 step
reversedTuple = my_tuple[::-1]

print(reversedTuple)

#Exercice2 : specific index in tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1].index(20))

#Exercice3 : create a tuple with only one item
new_tuple= (50, )
print(new_tuple)
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)
#Exercice3 : Swap two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple3 = ()

tuple3 = tuple1[:]
tuple1 = tuple2[:]
tuple2 = tuple3[:]


#OR
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)
#Exercice5:
tuple1 = (11, 22, 33, 44, 55, 66)
a = tuple1.index(44)
b = tuple1.index(55)
tuple2 = (tuple1[a], tuple1[b])
print(tuple2)
#exercice6 :
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

#Exercice8  :
tuple1 = (('a', 23) , ('b', 37) ,('c', 11), ('d',29))

myTuple = sorted(tuple1,key= lambda x:x[1])

print(myTuple)



