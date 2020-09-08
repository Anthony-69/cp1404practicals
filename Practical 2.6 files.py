# 1
out_file = open("names directory.txt", "w")
name = input("What is you name? ")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("names directory.txt", "r")
print("Your name is", name)
in_file.close()

# 3
out_file = open("numbers.txt", "w")
print(17, file=out_file)
print(42, file=out_file)
print(400, file=out_file)
out_file.close()

# 4
# ???