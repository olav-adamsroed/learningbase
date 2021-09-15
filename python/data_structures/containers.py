


#### This file will show various Python Container (Collection) Types ####

####  Dictionaries  ####
   #  Uses curly brackets {}
   #  

my_person = { 
    'first_name' : 'Olav',
    'last_name' : 'Adamsrød',
    'age' : 27,
    'profession' : ['Jr Security researcher', 'Student'],
    'relationship status' : 'taken',
}

print(my_person['first_name']+' '+my_person['last_name'])

for i in my_person['profession']:
    print(i)
print(len(my_person))


####  List  ####
   #  Square brackets []
   #  

""" my_list = ['one', 'two', 3]
print(my_list)
for element in my_list:
    print(element)
    if len(my_list) == 3:
        my_list.append('four')
    else:
        for jellyment in my_list:
            if len(my_list) == 4:
                my_list.append(5)
            else:
                print('Stoffers stive tiss')
                for jellybellyment in my_list:
                    if my_list[:-1] == 5:
                        print('shcmaker gut!')
                        my_list.append(6)
                    else:
                        print('break')
                        break
 
print('two' in my_list)
"""


####  Tuples  ####
   #  Tuples uses parentasis 
   #  Is immutable!!!

my_tuple = ('Oslo', 'Trondheim', 'Bergen', 'Kristiandsand', 'Tromsø', 'Stavanger')
print(my_tuple)
your_tuple = my_tuple
print(your_tuple)


####  Sets  ####
    #  Order in the tuples is not set in memory, so the order might when running
   #  uses squirly brackets {} 

my_set = {'Oslo', 'Trondheim', 'Bergen', 'Kristiandsand', 'Tromsø', 'Stavanger'}
my_set_2 = {'Tønsberg', 'Oslo', 'Kristiansand', 'Grimstad', 'Arendal', 'Porsgrunn'}

print(my_set)
print('Oslo' in my_set)
print(my_set.difference(my_set_2))
print(my_set.union(my_set_2))



#  Empty Lists
empty_list = []
empty_list = list()

#  Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This is not right, its a dict
empty_set = set()






