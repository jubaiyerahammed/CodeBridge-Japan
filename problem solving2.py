# -----------------------------------------
# ATTENDANCE TRACKING SYSTEM
# -----------------------------------------

# Sample attendance data for 5 students (Mon–Fri)
attendance = {
    "Alice": {
        "Mon": {"status": "Present", "late": 0},
        "Tue": {"status": "Late", "late": 10},
        "Wed": {"status": "Absent", "late": 0},
        "Thu": {"status": "Present", "late": 0},
        "Fri": {"status": "Late", "late": 5},
    },
    "Bob": {
        "Mon": {"status": "Absent", "late": 0},
        "Tue": {"status": "Present", "late": 0},
        "Wed": {"status": "Present", "late": 0},
        "Thu": {"status": "Late", "late": 15},
        "Fri": {"status": "Present", "late": 0},
    },
    "Charlie": {
        "Mon": {"status": "Present", "late": 0},
        "Tue": {"status": "Present", "late": 0},
        "Wed": {"status": "Late", "late": 7},
        "Thu": {"status": "Absent", "late": 0},
        "Fri": {"status": "Present", "late": 0},
    },
    "David": {
        "Mon": {"status": "Late", "late": 12},
        "Tue": {"status": "Present", "late": 0},
        "Wed": {"status": "Present", "late": 0},
        "Thu": {"status": "Present", "late": 0},
        "Fri": {"status": "Absent", "late": 0},
    },
    "Eva": {
        "Mon": {"status": "Present", "late": 0},
        "Tue": {"status": "Absent", "late": 0},
        "Wed": {"status": "Present", "late": 0},
        "Thu": {"status": "Late", "late": 20},
        "Fri": {"status": "Present", "late": 0},
    }
}

# -----------------------------------------
# FUNCTION 1: Check attendance of a student on a day
# -----------------------------------------
def check_attendance(student, day):
    record = attendance.get(student, {}).get(day)
    if not record:
        return "Record not found"
    return f"{student} was {record['status']} on {day}"

# -----------------------------------------
# FUNCTION 2: Get late-coming days for a student
# -----------------------------------------
def late_days(student):
    if student not in attendance:
        return "Student not found"

    result = []
    for day, info in attendance[student].items():
        if info["status"] == "Late":
            result.append((day, info["late"]))

    return result

# -----------------------------------------
# FUNCTION 3: Get list of absent students for a given day
# -----------------------------------------
def absentees(day):
    result = []
    for student, days in attendance.items():
        if days[day]["status"] == "Absent":
            result.append(student)
    return result

# -----------------------------------------
# MENU SYSTEM
# -----------------------------------------
def menu():
    while True:
        print("\n--- ATTENDANCE SYSTEM MENU ---")
        print("1. Check if a student was present on a day")
        print("2. Show late-coming days for a student")
        print("3. Show absent students for a day")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student = input("Enter student name: ")
            day = input("Enter day (Mon-Fri): ")
            print(check_attendance(student, day))

        elif choice == "2":
            student = input("Enter student name: ")
            result = late_days(student)
            if isinstance(result, str):
                print(result)
            else:
                print("Late days:", result)

        elif choice == "3":
            day = input("Enter day (Mon-Fri): ")
            print("Absent students:", absentees(day))

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Try again.")

# Run the menu
menu()
