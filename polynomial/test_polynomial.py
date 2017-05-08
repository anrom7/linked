from polynomial import Polynomial

poly1 = Polynomial()
poly2 = Polynomial()

data_file = open("data1.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly1._appendTerm(float(degree), float(coefficient))

data_file = open("data2.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly2._appendTerm(float(degree), float(coefficient))

print(poly1)
print(poly2)

print(poly1.degree())
print(poly2.degree())

print(poly1 + poly2)
print(poly1 - poly2)
print(poly1 * poly2)
