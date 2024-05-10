from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE)
    attendance_number = models.IntegerField()
    date_of_birth = models.DateField()
    enrollment_year = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'myhealthapp'

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100)
    grade = models.IntegerField()
    academic_year = models.IntegerField()

    def __str__(self):
        return f"{self.class_name} ({self.academic_year})"
    
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id.username} - {self.class_id.class_name}"
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # 実際の開発ではパスワードはハッシュ化して保存する
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class HealthRecord(models.Model):
    HEALTH_STATUS_CHOICES = [
        ('', ''),  # 初期値として空欄を設定
        ('sick', '病欠'),
        ('absent', '事故欠'),
    ]

    record_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    date = models.DateField()
    health_status = models.CharField(
        max_length=100,
        choices=HEALTH_STATUS_CHOICES,
        default='',  # 初期値を空欄に設定
    )

    def __str__(self):
        return f"{self.student_id.name} - {self.date} - {self.health_status}"