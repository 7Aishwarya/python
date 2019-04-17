java_course = {"John", "Jack", "Jill", "Joe"}
python_course = {"Jake", "John", "Eric", "Jill"}
print("Students enrolled for python course:",python_course)
print("Students enrolled for java course only:",java_course-python_course)
print("Students enrolled for python course only:",python_course-java_course)
print("Students enrolled for python and java course:",python_course&java_course)
a=python_course&java_course
b=python_course|java_course
c=(python_course|java_course)-(python_course&java_course)
print("Students enrolled for either Java or Python courses but not both:",c)
print("Students enrolled for either Java or Python courses:",b)
