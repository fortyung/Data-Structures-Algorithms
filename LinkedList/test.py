my_dict = {
    "value": 14,
    "next": {"value": 10, "next": {"value": 16, "next": {"value": 5, "next": None}}},
}

pre = my_dict

# Looking up the value of "key2" with a default value
for i in range(1):
    pre = pre["next"]


print(pre)
