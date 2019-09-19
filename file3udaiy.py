courses = {'python': 1500, 'java': 1000, 'c': 800, 'c++': 1200}



sort = sorted((value,key) for (key,value) in courses.items())

course={}

for i in sort:

    course[i[1]]=i[0]



print(course)
