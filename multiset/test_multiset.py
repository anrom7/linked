from multiset.multisetll import Multiset

data_set = Multiset()
data_file = open("data.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    data_set.add(line.strip())

value = input("Guess a value or type stop: ")
empty = False

while value != "stop" and not empty:
    if value in data_set:
        print("Yes, the set contains", value)
        data_set.delete(value)
    else:
        print("No, the set does not contain", value)
    if data_set.empty():
        print("Sorry, there are no values left to guess.")
        empty = True
    else:
        value = input("Guess a value or type stop: ")
