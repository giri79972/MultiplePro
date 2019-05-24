from django.db import models

# Create your models here.

# Create your models here.
class Customer(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=20)
    sales=models.IntegerField()
    def __str__(self):
        return self.cname
class Emp(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=20)
    sal=models.IntegerField()
    def __str__(self):
        return self.ename
class Student(Customer,Emp):
    sname=models.CharField(max_length=20)
    marks=models.IntegerField()
    def __str__(self):
        return self.sname
