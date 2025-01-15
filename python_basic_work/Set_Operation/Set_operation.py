# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
Union=set1|set2
print(Union)
print("Union:", union_set)

# Intersection of sets or we can use set1 & set2 And operator
intersection_set = set1.intersection(set2)
Intersect=set1&set2
print("Using And(&) operator :",Intersect)
print("Intersection:", intersection_set)

# Difference of sets
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

#add() method
set1.add(6)
print("After adding 6 in set1:",set1)

#update() method
set1.update([7,8,9])
print("After updating set1:",set1)

#remove() method it will raise an error if element is not present in set
set1.remove(8)
print("After removing 8 from set1:",set1)   

#discard() method it will not raise an error if element is not present in set   
set1.discard(13)
print("After discarding 9 from set1:",set1)

#isdisjoint() method    
set3={10,11,12}
print("Is set1 and set3 are disjoint:",set1.isdisjoint(set3))
#output: True

#issubset() method
set4={1,2,3,4,5,6,7,8,9}
print("Is set1 is subset of set4:",set1.issubset(set4))
#output: True

#issuperset() method means set4 is superset of set1 (set1 is subset of set4)
print("Is set4 is superset of set1:",set4.issuperset(set1))
#output: True