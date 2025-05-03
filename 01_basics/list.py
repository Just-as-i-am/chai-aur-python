tea_varieties = ["green", "black", "Oolong", "white"]
print(tea_varieties)
tea_varieties[0]
#accessing individual elements
print(tea_varieties[0])
#can also apply slicing
tea_varieties[0:3]
print(tea_varieties[0:3])
#lists are mutable
tea_varieties[1] ="herbal"
print(tea_varieties)
#can use slicing dicing to modify lists
tea_varieties[1:2] = "mint"
print(tea_varieties)
tea_varieties[1:2] ="chilly"
print(tea_varieties)
tea_varieties = ["black", "green", "mint", "white"]
tea_varieties[1:2] =["lemon"]
print(tea_varieties)
tea_varieties[1:3] = ["green", "Oolong"]
print(tea_varieties)
#use of loop to print individual elements of the list
for x in tea_varieties:
    print(x)
    
print("ist copy method")
tea_varieties_copy = tea_varieties  #using this copy procedure ,the copy variable will point to same memory reference of the source
print(tea_varieties_copy)
tea_varieties.pop()  # this change will also be reflected in copy variable
print("tea_varieties" ,tea_varieties)
print("tea_varieties_copy",tea_varieties_copy)

print("second copy method")
tea_varieties_copy = tea_varieties.copy() #using this copy method both are given separate memory references
tea_varieties[0] = "noon chai" #this will not be reflected in copy variable only in this variable its reflected
print("tea_varieties" ,tea_varieties)
print("tea_varieties_copy",tea_varieties_copy)