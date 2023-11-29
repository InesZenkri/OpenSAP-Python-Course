def get_student_data():
    name = input("Name?")
    nachname = input("Nachname?")
    student_id = input("Stud id?")
    return (name, nachname, student_id)

print(get_student_data())