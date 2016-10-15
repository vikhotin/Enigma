files = [str(i)+".txt" for i in range(6)]+["6.exe"]
#print(files)

for nm in files:
    f=open(nm,"rb")
    m=f.read()
    print(m)
'''
f=open("__testfile__","w",encoding="utf-8")
f.write("hey")
for i in range(256):
    try:
        #pass
        f.write(str(chr(i)))
        #print(str(chr(i)))
    except:
        print("Can't write symbol "+str(i))
f.close()
print("done")
'''
