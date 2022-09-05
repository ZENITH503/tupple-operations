#creating a tupple using ()
list =(1,2,3,4,5)
print(list)
# u cannot  change the elements of the tupple and it works as an array in the c++
list2 = (1) #throws a single elemnt but not with curly brackets
print(list2)
list3 = (1,) # now its a tupple of single elemnt
print(list3)
list4 =()
print(list4) #now its an empty tupple
print(list.count(4))#this takes the value and see the occurence of tht particular value
print(list.index(3))#this take the value nd return the index number of the enterd value,this searches for the value