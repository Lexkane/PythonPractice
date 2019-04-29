from django.db import models


def main():
    pass


class Student(models.Model):
    name = models.CharField(max_length=70)


s = Student(name='Alexey')
print(s.name)
