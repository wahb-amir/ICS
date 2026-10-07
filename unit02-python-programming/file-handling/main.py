FILE_NAME = "example.txt"
with open(FILE_NAME,"w") as f:
    f.write("hello world\n")
    
with open(FILE_NAME,"a") as f:
    f.write("Second line")

def read_file():
    with open(FILE_NAME,"r") as f:
        for line in f:
            yield line
line = read_file()
for n in line:
    print(n)
    
file = open(FILE_NAME,"r")


print("#"*40)
for n in file:
    print(n)
print("#"*40)

file.close()
