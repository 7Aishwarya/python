f1=open("d:\\testfile1.txt","r+")
f2=open("d:\\testfile.txt","w+")
line1=f1.read()
line2=f2.read()
f2.write(line1.replace('\"','\\\"'))
f1.close()
f2.close()


