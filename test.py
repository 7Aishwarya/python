import random
f1=open("d:\\project_text.txt","r+")
f2=open("d:\\project1_text.txt","w+")
line1=f1.read()
line2=f2.read()
a=(line1.lower().split())
print(a)
n=0
#def main():


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


for i in a:
    word = i
    print(i)
    f2.write(scramble(word))
    print(scramble(word),end=" ")
