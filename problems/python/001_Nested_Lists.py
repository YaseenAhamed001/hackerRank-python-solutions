# pylint: disable=W0106, C0103
''' URL:
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
'''

#Self Solution:

if __name__ == '__main__':
    python_students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
        scores.add(score)

    sorted_scores = sorted(list(scores))
    python_students.sort(key = lambda x : x[0])

    for i in python_students:
        print(i[0]) if i[1] == sorted_scores[1] else ""

########################################################################

#Optimized solution:

if __name__ == '__main__':
    python_students = []

    # Read input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])

    # Find second lowest score
    scores = {student[1] for student in python_students}  # set comprehension
    second_lowest = sorted(scores)[1]  # get second lowest

    # Sort students alphabetically and print those with second lowest score
    for student in sorted(python_students, key=lambda x: x[0]):
        if student[1] == second_lowest:
            print(student[0])
