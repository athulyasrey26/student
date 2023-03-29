from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Purpose(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Materials(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    

class Application(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    purpose =models.ForeignKey(Purpose, on_delete=models.RESTRICT)
    materials=models.ManyToManyField(Materials)

    def __str__(self):
        return self.name






