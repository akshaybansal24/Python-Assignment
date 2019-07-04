from compute import displayIndividualComponent, generateStudentsGrade, generateReport


def searchStudentByStudentId(studenid):
    for studentInfo in studentInfoList:
        if(studentInfo["studentId"]==studenid):
            return studentInfo
    return


def menu1():
    print("\t|----------------Enter the component----------------------")
    print("\t| A1 for Assignment 1")
    print("\t| A2 for Assignment 2")
    print("\t| PR for Project")
    print("\t| T1 for Test 1")
    print("\t| T2 for Test 2")
    print("\t ---------------------------------------------------------")
    selectedComponent = input("\tPlease enter component name").upper()
    if(selectedComponent in ("A1","A2","PR","T1","T2")):
        displayIndividualComponent(studentInfoList,maxMarksMap,selectedComponent)
        return
    print("\tInvalid Input!!!")
    menu1()

def menu2():
    print("\t|----------------Enter the component----------------------")
    print("\t| A1 for Assignment 1")
    print("\t| A2 for Assignment 2")
    print("\t| PR for Project")
    print("\t| T1 for Test 1")
    print("\t| T2 for Test 2")
    print("\t ---------------------------------------------------------")
    selectedComponent = input("\tPlease enter component name").upper()
    if (selectedComponent in ("A1", "A2", "PR", "T1", "T2")):
        displayIndividualComponent(studentInfoList, maxMarksMap, selectedComponent)
        return
    print("\tInvalid Input!!!")
    menu2()

def menu3():
    generateReport(studentInfoList)
    return
def menu4():
    return
def menu5():
    return
def menu6():
    return

classInfoFile = open("class.txt")
alMarkFile = open("a1.txt")
a2MarkFile = open("a2.txt")
test1File = open("test1.txt")
test2File = open("test2.txt")
projectFile = open("project.txt")

studentInfoList = []

for line in classInfoFile:
    studentInfo = line.rstrip().split("|")
    studentInfoMap = {"studentId":studentInfo[0],"firstName":studentInfo[1],"lastName":studentInfo[2]}
    
+.append(studentInfoMap)

maxA1 = alMarkFile.readline().rstrip()
for line in alMarkFile:
    a1Data = line.rstrip().split("|")
    studentInfo = searchStudentByStudentId(a1Data[0])
    studentInfo["A1"] = a1Data[1]

maxA2 = a2MarkFile.readline().rstrip()
for line in a2MarkFile:
    a2Data = line.rstrip().split("|")
    studentInfo = searchStudentByStudentId(a2Data[0])
    studentInfo["A2"] = a2Data[1]

maxT1 = test1File.readline().rstrip()
for line in test1File:
    t1Data = line.rstrip().split("|")
    studentInfo = searchStudentByStudentId(t1Data[0])
    studentInfo["T1"] = t1Data[1]

maxT2 = test2File.readline().rstrip()
for line in test2File:
    t2Data = line.rstrip().split("|")
    studentInfo = searchStudentByStudentId(t2Data[0])
    studentInfo["T2"] = t2Data[1]

maxProject = projectFile.readline().rstrip()
for line in projectFile:
    projectData = line.rstrip().split("|")
    studentInfo = searchStudentByStudentId(projectData[0])
    studentInfo["PR"] = projectData[1]

maxMarksMap = {"A1":maxA1,"A2":maxA2,"T1":maxT1,"T2":maxT2,"PR":maxProject}
sectionDistribution = {"A1":7.5,"A2":7.5,"T1":25,"T2":30,"PR":30}
generateStudentsGrade(studentInfoList, maxMarksMap, sectionDistribution,50)

userInput =0
menu = {1 : menu1,
        2 : menu2,
        3 : menu3,
        4 : menu4,
        5 : menu5,
        6 : menu6
}	
while(userInput!=6):
    print("----------------Menu---------------")
    print("1> Display individual component")
    print("2> Display component average")
    print("3> Display Standard Report")
    print("4> Sort by alternate column")
    print("5> Change Pass/Fail point")
    print("6> Exit")
    print("----------------------------------")
    try:
        userInput = int(input("Enter your choice"))
        menu[userInput]()
    except(Exception) as e:
        print("Invalid Input")
