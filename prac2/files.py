name=input("name:")
write_names_file=open("names.txt","w")
print(name,file=write_names_file)
write_names_file.close()
read_names_file=open("names.txt","r")
line=read_names_file.readline()
print('your name is {}'.format(line))
read_names_file.close()

""" gets name writes it to file, reads same file and prints name"""

numbers_file=open("number.txt","r")
numbers = numbers_file.readlines()
total=sum(numbers)
print(total)
numbers_file.close()