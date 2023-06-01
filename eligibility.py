import sys
students = sys.stdin.read().splitlines()
students.pop(0)
for student in students:
    details = student.split()
    studyyear = int(details[1].split('/')[0])
    dobyear = int(details[2].split('/')[0])
    if studyyear >= 2010 or dobyear >= 1991:
        elig = 'eligible'
    elif int(details[3]) > 40:
        elig = 'ineligible'
    else:
        elig = 'coach petitions'
    print(details[0], elig)