import random

def generate_testcase(num_professors, num_courses, compulsory_courses, elective_courses):
    professors = [f"prof{i}" for i in range(1, num_professors + 1)]
    courses = [f"course{i}" for i in range(1, num_courses + 1)]

   
    preferences = {prof: random.choice([0.5, 1, 1.5]) for prof in professors}

   
    testcases = []
    for prof in professors:
        selected_courses = random.sample(compulsory_courses + elective_courses, random.randint(1, len(compulsory_courses) + len(elective_courses)))
        testcases.append([prof] + selected_courses)

    return preferences, testcases

def print_testcase_to_file(preferences, testcases, compulsory_courses, elective_courses, filename):
    with open(filename, 'w') as file:
        file.write(','.join(f"{prof}:{preferences[prof]}" for prof in preferences) + '\n')
        file.write(f"compulsory:{'|'.join(course for course in compulsory_courses)}")
        if elective_courses:
            file.write(f",elective:{'|'.join(course for course in elective_courses)}")
        file.write('\n')
        for testcase in testcases:
            file.write(','.join(testcase) + '\n')


num_professors = 4
num_courses = 5
compulsory_courses = ["course1", "course2", "course3"]
elective_courses = ["course4", "course5", ]
output_filename = 'testcase.txt'

preferences, testcases = generate_testcase(num_professors, num_courses, compulsory_courses, elective_courses)
print_testcase_to_file(preferences, testcases, compulsory_courses, elective_courses, output_filename)
