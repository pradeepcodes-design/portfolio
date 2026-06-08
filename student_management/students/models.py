from django.db import models

class Student(models.Model):
    register_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.register_number} - {self.name}"

class Marks(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='marks')
    subject1 = models.IntegerField(default=0)
    subject2 = models.IntegerField(default=0)
    subject3 = models.IntegerField(default=0)
    subject4 = models.IntegerField(default=0)
    subject5 = models.IntegerField(default=0)

    @property
    def total(self):
        return self.subject1 + self.subject2 + self.subject3 + self.subject4 + self.subject5

    @property
    def percentage(self):
        return round((self.total / 500) * 100, 2)

    @property
    def is_pass(self):
        return all(m >= 35 for m in [self.subject1, self.subject2, self.subject3, self.subject4, self.subject5])

    @property
    def result(self):
        return "Pass" if self.is_pass else "Fail"

    @property
    def grade(self):
        if not self.is_pass:
            return "F"
        p = self.percentage
        if p >= 90: return "A+"
        if p >= 80: return "A"
        if p >= 70: return "B+"
        if p >= 60: return "B"
        if p >= 50: return "C+"
        return "C"

    def __str__(self):
        return f"Marks - {self.student.register_number}"
