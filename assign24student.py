student={"John":86.5, "Jack":91.2, "Jill":84.5, "Harry":72.1, "Joe":80.5}
for key in student:
    print(key,": ", student[key])
l=student.copy()
l=sorted(l.values(),reverse=True)
print("Top two scoreres of the course are:")
for key,value in student.items():
    if(student[key]==l[0] or student[key]==l[1]):
        print(key,value)
print("Class average of this course:",sum(l)/len(l))
