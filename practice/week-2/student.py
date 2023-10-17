class Student:
    def __init__(self, name, education, email, legs, id):
        self.name = name
        self.education = education
        self._email = email
        self._legs = legs
        self._id = id

    @property
    def email(self):
        return self._email

    @email.setter
    def set_email(self, new_email):
        if type(new_email) == str and "@school.org" in new_email:
            self._email = new_email

    @property
    def legs(self):
        return self._legs

    @property
    def id(self):
        return self._id

    @id.setter
    def set_id(self, new_id):
        if len(new_id) == 8 and not new_id[0].isnumeric():
            self._id = new_id

    def go_to_school(self):
        print(f"{self.name} going to school!")

    def __str__(self):
        return f"{self.name} | {self.education} | {self.email} | {self.id}"


# name, education, email, legs, id
student_one = Student("Mike", "High School", "mike@school.org", 3, "m2345678")

print(student_one.id)
student_one.set_id = "m43fosin"
print(student_one.id)
print(student_one)
