txt2 = input("Digite uma palavra: ")
i = 6
txt = [txt2]
print(txt)
for x in range(0,i,1):
    txt.append(txt2)
for x in range(0,i+1,1):
    print(txt)