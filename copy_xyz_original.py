file_name=input("Enter the file name:")
import random
f1=open("d:\\"+file_name+".txt","r+")
f2=open("d:\\"+file_name+"Scrambled"+".txt","w+")
line1=f1.read()
line2=f2.read()
a=(line1.split())
n=0
c=0
def main():
    for i in a:
        if(i[-1]=="," or i[-1]==";" or i[-1]=="!" or i[-1]=="?" or i[-1]=="."):
            j=i[-1]
            i=i[0:-1]
            if(len(i)>3):
                word = i
                f2.write(scramble(word))
                f2.write(j)
                f2.write(" ")
                print(scramble(word), end="")
                print(j, end=" ")
            else:
                f2.write(i)
                f2.write(j)
                f2.write(" ")
                print(i,end="")
                print(j, end=" ")
        elif(len(i)>3):
            word = i
            f2.write(scramble(word))
            f2.write(" ")
            print(scramble(word),end=" ")
        else:
            f2.write(i)
            f2.write(" ")
            print(i, end=" ")
            

def scramble(word):
    char1 = random.randint(1, len(word)-2)
    char2 = random.randint(1, len(word)-2)
    while char1 == char2:
        char2 = random.randint(1, len(word)-2)
    newWord = ""

    for i in range(len(word)):
        if i == char1:
            newWord = newWord + word[char2]
        elif i == char2:
            newWord = newWord + word[char1]
        else:
            newWord = newWord + word[i]

    return newWord

main()
f1.close()
f2.close()
