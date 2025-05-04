#defining dictionary
chai_types = {"masala":"spicy", "ginger":"zesty", "green":"mild"}
#accesing elements
print(chai_types["ginger"])      #using this method if we access any key that is not present in dictionary will give keyError

print(chai_types.get("gingery"))   #if we access wrong key it will not give error but will return none
chai_types["green"] = "fresh"
print(chai_types)

#using loops
for chai in chai_types:
        print(chai, chai_types[chai])

for key, value in chai_types.items():
        print(key,value)
#adding or removing elements in the dictionary
print(chai_types)
chai_types["lemon"] = "delicious"
print(chai_types)
chai_types.popitem()
print(chai_types)
chai_types.pop("masala")
print(chai_types)
del chai_types["green"]
print(chai_types)

#nesting in dictionary
tea_shop = {"chai": {"masala": "spicy", "ginger": "zesty" , "green":"mild" },
            "tea":{"black": "strong", "Lemon": "yummy"}}
print(tea_shop["chai"]["masala"])

#dictionary comprehension
square_num ={ x: x**2 for x in range(6)}
print(square_num)

#constructing dict from key set and value set
keys = ["masala", "ginger", "green"]
default_value = "delicious"
new_dictionary = dict.fromkeys(keys, default_value)
print(new_dictionary)