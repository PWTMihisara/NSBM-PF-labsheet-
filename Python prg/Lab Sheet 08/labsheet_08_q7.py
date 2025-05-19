def qualityPoints(avg):

    if avg >= 90:
        point = 4
    elif avg >= 80:
        point = 3
    elif avg >= 70:
        point = 2
    elif avg >= 60:
        point = 1
    else:
        point = 0

    return point

avg = float(input("Enter the student's average : "))

print(f"The quality points of the student : {qualityPoints(avg)}")