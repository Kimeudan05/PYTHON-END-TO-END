import json

class Student:
    def __init__(self, name, age, grade, subjects=None):
        self.__name = name
        self.__age = age
        self.__grade = grade
        self.__subjects = subjects if subjects else {}  # e.g., {"Math": 90}
        
    # properties
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age

    @property
    def grade(self):
        return self.__grade



    def __str__(self):
        subjects_str = ', '.join(f"{sub}: {score}" for sub, score in self.__subjects.items())
        return f"{self.__name}, Grade: {self.__grade}, Age: {self.__age}, Subjects: [{subjects_str}]"

    def update_grade(self, new_grade):
        self.__grade = new_grade

    def update_subject_score(self, subject, score):
        self.__subjects[subject] = score

    def delete_subject(self, subject):
        if subject in self.__subjects:
            del self.__subjects[subject]

    def _is_minor(self):
        return self.__age < 18

    def to_dict(self):
        return {
            "name": self.__name,
            "age": self.__age,
            "grade": self.__grade,
            "subjects": self.__subjects
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["grade"], data.get("subjects", {}))

    @staticmethod
    def add_student():
        try:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            subjects = {}

            while True:
                add_subj = input("Add a subject? (yes/no): ").lower()
                if add_subj == 'no':
                    break
                subject = input("Subject name: ")
                score = float(input("Score: "))
                subjects[subject] = score

            return Student(name, age, grade, subjects)
        except ValueError:
            print("Invalid input.")
            return None

# Global student list
students = []

# File save/load
def save_to_file(filename="students.json"):
    with open(filename, "w") as f:
        json.dump([s.to_dict() for s in students], f)
    print("Data saved to file.")

def load_from_file(filename="students.json"):
    global students
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            students = [Student.from_dict(s) for s in data]
        print("Data loaded from file.")
    except FileNotFoundError:
        print("No saved data found.")

# Menu system
def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Grade")
        print("4. Update Subject Score")
        print("5. Delete Student")
        print("6. Save to File")
        print("7. Load from File")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student = Student.add_student()
            if student:
                students.append(student)

        elif choice == "2":
            if not students:
                print("No students to display.")
            else:
                for i, s in enumerate(students):
                    print(f"{i + 1}. {s}")

        elif choice == "3":
            index = int(input("Enter student number to update grade: ")) - 1
            if 0 <= index < len(students):
                new_grade = input("Enter new grade: ")
                students[index].update_grade(new_grade)
                print("Grade updated.")
            else:
                print("Invalid student number.")

        elif choice == "4":
            index = int(input("Enter student number to update subject score: ")) - 1
            if 0 <= index < len(students):
                subject = input("Enter subject: ")
                score = float(input("Enter new score: "))
                students[index].update_subject_score(subject, score)
                print("Subject score updated.")
            else:
                print("Invalid student number.")

        elif choice == "5":
            index = int(input("Enter student number to delete: ")) - 1
            if 0 <= index < len(students):
                confirm = input(f"Are you sure you want to delete {students[index].name}? (yes/no): ")
                if confirm.lower() == "yes":
                    del students[index]
                    print("Student deleted.")
            else:
                print("Invalid student number.")

        elif choice == "6":
            save_to_file()

        elif choice == "7":
            load_from_file()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run the menu
if __name__ == "__main__":
    menu()
