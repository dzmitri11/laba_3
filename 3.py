File = open("subjects.txt", "r")
dict = {}	
for line in File:
    words = line.split(":")
    if len(words) == 2:
        nameLesson = words[0]
        lessonInfo = words[1]
        lessonParts = lessonInfo.split()
        lessonTotal = sum(int(part.split("(")[0]) for part in lessonParts)
        dict[nameLesson] = lessonTotal
print(dict)