n =(input("Enter the text  "))
listed = []
count=0
for i in range(len(n)):
    name = input("Enter the letter")
    listed.append(name)
for i in listed:
    for j in i:
        if(j== na):
            count=count+1
print(count)
