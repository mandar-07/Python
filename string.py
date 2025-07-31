name=input("Enter any string ")

print(name)

print(name.upper())
print(name.lower())
print(name.__len__())
print(name.find("m"))
print(name.index("d"))
print(name.strip())
print(name.count("a"))
print(name.endswith('r'))
print(name.title())
print(name +" patil")
print(name.isdigit())
print(name.isalpha())
print(name.isascii())
print(name.islower())


for x in name:
    print(x)

print(name[1:5])
print(name[-5:5:2])
print(name[1:6])
print(name[0:5])
print(name[-5:-2])
print(name[-5:-3])