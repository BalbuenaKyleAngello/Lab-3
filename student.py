# student.py

class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """Test for equality"""
        return self.name == other.name

    def __lt__(self, other):
        """Test for less than"""
        return self.name < other.name

    def __ge__(self, other):
        """Test for greater than or equal to"""
        return self.name >= other.name

def main():
    student1 = Student("Alice")
    student2 = Student("Alice")
    student3 = Student("Alice")

    print("Equality test:")
    print(student1 == student2)  # Should print False
    print(student1 == student3)  # Should print True

    print("\nLess than test:")
    print(student1 < student2)  # Should print True
    print(student2 < student1)  # Should print False

    print("\nGreater than or equal to test:")
    print(student1 >= student2)  # Should print False
    print(student2 >= student1)  # Should print True
    print(student1 >= student3)  # Should print True

if __name__ == "__main__":
    main()
