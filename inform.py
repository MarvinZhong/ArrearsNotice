def inform(): #main statement
    n = int(input()) #input n value
    list1 = list() #create list for id name and salary
    list2 = list() #create list for married person
    loop = 0 #loop = 0
    while loop < n: #while loop lessthan n value
        list1.append(list(map(str,input().split()))) #input id name and salary
        list1[loop][2] = int(list1[loop][2]) #list1[loop][2] = int(list1[loop][2])
        loop += 1 #loop = loop + 1
    m = int(input()) #input m value
    loop = 1 # loop = 1
    while loop <= m: #while loop lessthan m
        list2.append(list(map(str, input().split()))) #input for id name and id name
        loop += 1 #loop = loop + 1
    list1.sort(key=lambda x: int(x[2]), reverse=True) #function for sortting
    for i in range(200) : #range for rich people
        for j in range(m) : #range for married people
            if list1[i][0] == list2[j][0] : #statement if list1[i][0] == list2[j][0]
                for both in range(n) : #checking for rich and married people
                    if list2[j][2] == list1[both][0] and list1[both][2] > 500000 : #statement for checking first people
                        print(list1[both][0],list1[both][1]) #print out first people
            elif list1[i][0] == list2[j][2] : #statement if list1[i][0] == list2[j][2]
                for both in range(n) : #checking for rich and married people
                    if list2[j][0] == list1[both][0] and list1[both][2] > 500000 : #statement for checking second people
                        print(list1[both][0],list1[both][1]) #print out second people
inform() #run main statement
