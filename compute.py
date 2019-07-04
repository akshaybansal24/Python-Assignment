def displayIndividualComponent(studentInfoList, maxGradeMap,selectedComponent):
    print("==================================================")
    print(selectedComponent+" grades ("+maxGradeMap[selectedComponent]+")")
    for studnetInfo in studentInfoList:
        print(studnetInfo["studentId"]+"\t"+studnetInfo["lastName"]+","+studnetInfo["firstName"]+"\t\t"+studnetInfo[selectedComponent])
    print("==================================================")
    return

def displayAvgComponent(studentInfoList, maxGradeMap,selectedComponent):
    print("==================================================")
    componentSum =0
    componentCounter=0
    for studnetInfo in studentInfoList:
        try:
            componentSum = componentSum+ studnetInfo[selectedComponent]
            componentCounter = componentCounter+ 1
        except KeyError:
            pass
    print("==================================================")
    avg = componentSum/componentSum
    print(selectedComponent+" Average: "+str(round(avg,2))+"/"+maxGradeMap[selectedComponent])
    return

def generateStudentsGrade(studentInfoList, maxGradeMap, sectionDistribution, passLimit):
    gradeRange = (100-passLimit)/7
    for studentInfo in studentInfoList:
        percentage =0
        for section in sectionDistribution:
            try:
                percentage = percentage + int(studentInfo[section])/int(maxGradeMap[section])*sectionDistribution[section]
            except (KeyError,Exception):
                pass
        studentInfo["percentage"]=percentage
        if(percentage<passLimit):
            studentInfo["grade"]="F"
        elif(percentage<passLimit+gradeRange):
            studentInfo["grade"]="C"
        elif(percentage<passLimit+(2*gradeRange)):
            studentInfo["grade"]="B-"
        elif(percentage<passLimit+(3*gradeRange)):
            studentInfo["grade"]="B"
        elif(percentage<passLimit+(4*gradeRange)):
            studentInfo["grade"]="B+"
        elif(percentage<passLimit+(5*gradeRange)):
            studentInfo["grade"]="A-"
        elif(percentage<passLimit+(6*gradeRange)):
            studentInfo["grade"]="A"
        else:
            studentInfo["grade"]="A+"
    return

def generateReport(studentInfoList):
    print("ID\tLN\FN\tA1\tA2\tPR\tT1\tT2\tGR\FL")
    for studentInfo in studentInfoList:
        a1Score=0
        a2Score=0
        prScore=0
        t1Score=0
        t2Score=0
        try:
            a1Score = studentInfo["A1"]
        except KeyError:
            a1Score = 0
        try:
            a2Score = studentInfo["A2"]
        except KeyError:
            a2Score = 0
        try:
            t1Score = studentInfo["T1"]
        except KeyError:
            t1Score = 0
        try:
            t2Score = studentInfo["T2"]
        except KeyError:
            t2Score = 0
        try:
            prScore = studentInfo["PR"]
        except KeyError:
            prScore = 0

        print(studentInfo["studentId"]+"\t"+studentInfo["lastName"]+"\t"+studentInfo["firstName"]+"\t"+a1Score+"\t"+a2Score+"\t"+prScore+"\t"+t1Score+"\t"+t2Score+"\t"+str(round(studentInfo["percentage"],2))+"\t"+studentInfo["grade"])
    return
