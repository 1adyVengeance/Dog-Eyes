from django.db import models

# Create your models here.
class Shop_employee(models.Model):
    name = models.CharField(max_length=64,null=False)
    emp_no = models.CharField(max_length=64,null=True)
    sex = models.BooleanField(null=False)
    age = models.IntegerField(null=True)
    join_time = models.DateTimeField(null=True)
    work_status = models.CharField(max_length=32,null=True)
    salary = models.IntegerField(null=True)
    subsidy = models.IntegerField(null=True)
    work_time = models.IntegerField(null=True)
    store_role_id = models.IntegerField(null=False)
    password = models.CharField(max_length=128,null=False)
    store_id = models.IntegerField(null=False)

    class Meta:
        db_table = 'emp_info'
















