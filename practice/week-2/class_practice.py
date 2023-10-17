class Student:
    all_students = {}
    id = 0

    def __init__(self, name, email):
        Student.id += 1
        self.name = name
        self._id = Student.id
        self._email = email
        Student.all_students[self._id] = self

    def __str__(self):
        return f"NAME: {self.name} | ID: {self._id} | EMAIL: {self._email}"

    @property
    def get_id(self):
        return self._id

    @get_id.setter
    def set_id(self, new_id):
        if new_id.isnumeric():
            self._id = new_id

    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def set_email(self, new_email):
        valid = "@student.org"
        if valid in new_email[: -len(valid)]:
            self._email = new_email

    # instance method
    # going to school
    def go_to_school(self):
        return f"{self.name} is going to school."

    # studying
    def start_studying(self):
        return f"{self.name} is starting to study!"

    @classmethod
    def add_a_student(cls):
        name = input("Student name: ")
        email = name + "@student.org"
        cls(name, email)
        print(cls.all_students)

    @classmethod
    def view_all_students(cls):
        for student in cls.all_students.values():
            print(student)
            # for dictionaries, use .values or get. to pull values
            # instead of all_students[student]

    # staticmethod points to class or instance, and does not take argument. Used when you are not altering the attributes
    @staticmethod
    def view_all_students():
        for student in Student.all_students.values():
            print(student)


student1 = Student("Bob", "bob@gmail.com")
print(student1.get_id)
