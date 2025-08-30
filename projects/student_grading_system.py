name = input("Enter the name of the student :")
score  = int(input("Enter the score of the student :"))
def calculate_grade(score):
    match score :
        case m if 90<=m<=100:
            return "A"
        case m if 75 <= m:
            return "B"
        case m if 60 <= m :
            return "C"
        case m if 40 <= m :
            return "D"
        case m if 0 <= m < 40:
            return "F"
def generate_student_report(name , score ):
    grade = calculate_grade(score)
    print(f"{name} has scored {score} and received grade {grade}")

generate_student_report(name,score)