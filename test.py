"""Student grade tracking system."""


class Student:
    """Represent a student and manage their grades."""

    def __init__(self, student_id, name):
        """Initialize a student record with an ID and a name."""
        if not student_id or not str(student_id).strip():
            raise ValueError("Student ID cannot be empty.")
        if not name or not str(name).strip():
            raise ValueError("Student name cannot be empty.")

        self.id = str(student_id).strip()
        self.name = str(name).strip()
        self.grades = []
        self.is_passed = False
        self.honor = "?"

    def add_grade(self, grade):
        """Add a numeric grade within the valid range."""
        try:
            numeric_grade = float(grade)
        except (TypeError, ValueError):
            print("Error: grade must be numeric.")
            return False

        if not 0 <= numeric_grade <= 100:
            print("Error: grade must be between 0 and 100.")
            return False

        self.grades.append(numeric_grade)
        return True

    def calculate_average(self):
        """Calculate the average of all valid grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        """Return the letter grade based on the average."""
        average = self.calculate_average()
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def determine_pass_fail(self):
        """Set and return the pass/fail status."""
        self.is_passed = self.calculate_average() >= 60
        return self.is_passed

    def check_honor(self):
        """Determine whether the student qualifies for honor status."""
        if self.calculate_average() >= 90:
            self.honor = "Honor Student"
        else:
            self.honor = "No honor"
        return self.honor

    def delete_grade(self, index):
        """Delete a grade from the list at the given index."""
        if index < 0 or index >= len(self.grades):
            print("Error: invalid grade index.")
            return False
        del self.grades[index]
        return True

    def report(self):
        """Print the student summary with average and status."""
        average = self.calculate_average()
        letter_grade = self.determine_letter_grade()
        status = "Passed" if self.determine_pass_fail() else "Failed"
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"Status: {status}")


def main():
    """Run the student system demo."""
    print("Student system demo")
    print("-" * 30)

    try:
        student_one = Student("S001", "Ana")
    except ValueError as exc:
        print(f"Error: {exc}")
        student_one = None

    if student_one is not None:
        student_one.add_grade(95)
        student_one.add_grade(88)
        student_one.add_grade(70)
        student_one.add_grade("bad")
        student_one.add_grade(110)
        student_one.delete_grade(2)
        student_one.check_honor()
        student_one.report()

    print("-" * 30)
    try:
        Student("", "Luis")
    except ValueError as exc:
        print(f"Error: {exc}")

    try:
        Student("S002", "Maria")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
