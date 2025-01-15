# write max,min,sum,len,sorted
set1={10,8,9,3,40,5}
set2={11,12,4,5,6,7,8}
set3={10,11,12}
#max
print("Maximum element in set1:",max(set1))
#output: 40


#min
print("Minimum element in set1:",min(set1))
#output: 1
#another way to find  max and min element
#for max
sorted_min=sorted(set1)
print("Maximum element in set1:",sorted_min[-1]) #output: 40
#for min
sorted_min=sorted(set1)
print("Minimum element in set1:",sorted_min[0]) #output: 1

#sum
print("Sum of elements in set1:",sum(set1))
#output: 66


#len
print("Length of set1:",len(set1))
#output: 6

#sorted
print("Sorted set1:",sorted(set1))
#output: [1, 3, 5, 8, 9, 40]


#clear
set1.clear()
print("After clearing set1:",set1)
#output: set()


#write a program find common elements in set1 and set2 and set3
set1={11,8,9,3,12,40,5}
set2={11,12,4,5,6,7,8}
set3={10,11,12}
#common elements in set1 and set2
common=set1.intersection(set2,set3)
print("Common elements in set1 and set2 and set3:",common)
#output: {11, 12}

#write a program find difference elements in set1 and set2 and set3
set1={11,8,9,3,12,40,5}
set2={11,12,4,5,6,7,8}
set3={10,11,12}
#difference elements in set1 and set2
diff=set1.difference(set2,set3)
print("Difference elements in set1 and set2 and set3:",diff)    
#output: {40, 3, 8, 9}

#write a program find to remove elements in set1 and set2 and set3 if it is present
set1={11,8,9,3,12,40,5}
set2={11,12,4,5,6,7,8}
set3={10,11,12}
#remove elements in set1 and set2
set1.difference_update(set2,set3)
print("After removing elements in set1 and set2 and set3:",set1)
#output: {40, 3, 8, 9}

#to remove elements in set1 and set2 and set3 if it is present
set4={11,8,9,3,12,40,5,20,86}
remove_set_elemenet=set4.remove(40)
print("After removing elements in set1:",set4)
#output: {3, 5, 8, 9, 11, 12, 20, 86}


#to remove elements in set1 and set2 and set3 if it is present not present in set but it dont give error
set4={11,8,9,3,12,40,5,20,86}
remove_set_elemenet=set4.discard(100)
print("After removing elements in set1:",set4)
#output: {3, 5, 8, 9, 11, 12, 40, 20, 86}