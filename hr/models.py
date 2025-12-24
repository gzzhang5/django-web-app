from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(max_length=6, unique=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    access_level = models.CharField(max_length=10)
    work_status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"
