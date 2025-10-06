# START
testScoreString = '87'
classRankString = '60'
testScore = int(testScoreString)
classRank = int(classRankString)
print("=== College Admission Program ===")
print("Enter Test Score:")
print(testScoreString)
print("Enter Class Rank:")
print(classRankString)
print()
print(f"Test Score: {testScore}")
print(f"Class Rank: {classRank}")
print()

if testScore >= 90:
    if classRank >= 25:
        print("Accept")
    else:
        print("Reject")
else:
    if testScore >= 80:
        if classRank >= 50:
            print("Accept")
        else:
            print("Reject")
    else:
        if testScore >= 70:
            if classRank >= 75:
                print("Accept")
            else:
                print("Reject")
        else:
            print("Reject")
# STOP