"""
Student Attendance Record I

You are given a string s representing an attendance record for a student where each character signifies whether
the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.
"""
def attendance_record(report):

    counter = 0

    for i in range(len(report)):
        if report[i] == 'P':
            continue

        if report[i] == 'A':
            counter += 1
            if counter > 1:
                return False
                break

        if report[i] == 'L':
            try:
                if report[i + 1] == 'L' and report[i + 2] == 'L':
                    return False
            except IndexError:
                return True


    return True

report = "PPALLA"
print(attendance_record(report))










