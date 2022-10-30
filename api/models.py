from django.db import models

# Create your models here.


class Institute(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    abbreviation = models.CharField(
        max_length=10, null=False, blank=False, unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    abbreviation = models.CharField(
        max_length=10, null=False, blank=False, unique=True)
    institute = models.ForeignKey('Institute', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CourseType(models.Model):
    degree_level = models.CharField(choices=[
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('PHD', 'Doctorate'),
        ('DIP', 'Diploma'),
    ], max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.degree_level


class Course(models.Model):
    course_id = models.CharField(
        max_length=10, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    abbreviation = models.CharField(
        max_length=10, null=False, blank=False, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    type = models.ForeignKey('CourseType', on_delete=models.CASCADE, null=True)
    total_semesters = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name


class SubjectType(models.Model):
    SUBJECT_TYPE_CHOICES = [
        ('P', 'Practical'),
        ('T', 'Theory'),
    ]
    type = models.CharField(choices=SUBJECT_TYPE_CHOICES,
                            max_length=10, null=False, blank=False)

    def __str__(self):
        if self.type == 'P':
            return 'Practical'
        elif self.type == 'T':
            return 'Theory'
        else:
            return 'Unknown'


class Subject(models.Model):
    code = models.CharField(max_length=10, null=False,
                            blank=False, unique=True)
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    abbreviation = models.CharField(
        max_length=10, null=False, blank=False, unique=True)
    type = models.ForeignKey(
        'SubjectType', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=100, unique=True)
    branch = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length=13, unique=True, null=True)
    email = models.EmailField(max_length=100, unique=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.enrollment}"


class FacultyType(models.Model):
    TYPE_CHOICES = [
        ('PRINCIPAL', 'Principal'),
        ('HOD', 'Head of Department'),
        ('FAC', 'Faculty'),
        ('VF', 'Visiting Faculty'),
        ('RF', 'Research Faculty'),
        ('AF', 'Adjunct Faculty'),
        ('PF', 'Part Time Faculty'),
        ('ASST', 'Assistant'),
        ('LAB ASST.', 'Lab Assistant'),
        ('LAB ATT.', 'Lab Attendant'),
        ('LAB INCH.', 'Lab Instructor'),
        ('LAB TECH.', 'Lab Technician'),
        ('LAB SUPER.', 'Lab Supervisor'),
        ('LAB COORD.', 'Lab Coordinator'),
        ('LAB MANAGER', 'Lab Manager'),
    ]
    type = models.CharField(choices=TYPE_CHOICES,max_length=100, null=False,
                            blank=False, unique=True)

    def __str__(self):
        return self.type

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    faculty_id = models.CharField(max_length=100, unique=True)
    type = models.ForeignKey('FacultyType', on_delete=models.CASCADE, null=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)
    address = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length=13, unique=True, null=True)
    email = models.EmailField(max_length=100, unique=True, null=True)

    def __str__(self):
        return f"({self.faculty_id}) {self.name}"

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"


class ClassRoomType(models.Model):
    type = models.CharField(choices=[
        ('P', 'Practical'),
        ('T', 'Theory'),
    ], max_length=100, null=False, blank=False, unique=True)


class ClassRoom(models.Model):
    room_number = models.CharField(
        max_length=10, null=False, blank=False, unique=True)
    type = models.ForeignKey(
        'ClassRoomType', on_delete=models.CASCADE, null=True)
    capacity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
