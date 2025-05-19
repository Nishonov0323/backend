from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    days = models.CharField(max_length=100)
    weekly_classes = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

class Student(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    school = models.CharField(max_length=200, null=True)
    village = models.CharField(max_length=100, null=True)
    grade = models.CharField(max_length=50, null=True)
    knowledge_level = models.CharField(max_length=50, null=True)
    available_days = models.CharField(max_length=100, null=True)
    secondary_phone = models.CharField(max_length=20, null=True)
    trial_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='trial_students')
    trial_start = models.DateField(null=True)
    trial_end = models.DateField(null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    experience = models.IntegerField(null=True)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    max_groups = models.IntegerField(null=True)
    trial_start = models.DateField(null=True)
    trial_end = models.DateField(null=True)
    salary_percentage = models.FloatField(null=True)
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class LeaveRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()
    teacher_approved = models.BooleanField(default=False)
    admin_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.date}"

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    check_file = models.CharField(max_length=200, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.amount}"