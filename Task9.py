def main():
    # Step 1: Create a dictionary with student names and marks
    student_marks = {
        "Alice": 91,
        "Bob": 84,
        "Charlie": 76,
        "Diana": 88,
        "Eve": 95
    }

    # Step 2: Ask the user for a student's name
    name = input("Enter the student's name: ")

    # Step 3 & 4: Retrieve marks or handle missing name
    if name in student_marks:
        print(f"{name}'s marks: {student_marks[name]}")
    else:
        print(f"Student '{name}' not found in the records.")

if __name__ == "__main__":
    main()
