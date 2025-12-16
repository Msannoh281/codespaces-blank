# GPA calculator
# 1. need to take in user input for subject- can be any school subject
# 2. need to take ina grade 17 times. each  grade representin each week in the 
# semester.
# 3. once I have all 17 grades, I need to add them up, and then divide by 17
# 4. one I have the number grade, I need to write some codes to transform


def gpaCalculator():
    print(' What subject is this GPA for? ')
    subject = input()
    print("the user entered "+ subject)

week = 1
while week != 17:
    print(' please ebter the grade for this week : '+ str(week))
    grade = input()
    #print(grade)
    sum += grade
    #print(sum)
    week += 1
    gpa = sum / 10
    if gpa > 70 and < 80
        print('C')
    elif gpa > 80 and < 90
        print('B')
    elif gpa > 90 and < 100
        print('A')

    print('your gpa for'+ subject 'is ' + str(gpa))