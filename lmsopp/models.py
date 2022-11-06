from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    """ User Manager that knows how to create users via email instead of username """
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)


class Course(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.title} {self.date}'

    def get_absolut_url(self):
        return reverse('lms/home.html', args=[str(self.id)])


class Client(AbstractUser):
    first_name = models.CharField(max_length=50, )
    email = models.EmailField("email address", blank=False, null=False, unique=True, )

    class Meta:
        abstract = True

    def __str__(self):
        if self.first_name:
            return self.first_name
        else:
            return self.username


class Student(Client):
    course = models.ManyToManyField(Course, related_name='StudentCourse', blank=True)
    groups = ['students']
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    username = None

    objects = UserManager()


class Teacher(Client):
    course = models.ManyToManyField(Course, related_name='TeacherCourse',  blank=True)
    groups = ['teachers']


class Payment(models.Model):
    expired_date = models.DateField()
    price = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='CoursePayment', )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='CourseStudent', )


class Task(models.Model):
    description = models.TextField()
    image = models.ImageField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='CourseTask', )
