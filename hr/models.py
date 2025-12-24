from django.db import models

class Employee(models.Model):
    ACCESS_LEVEL_CHOICES = [
        ('LAB', 'Lab'),
        ('PROD', 'Production'),
    ]
    
    WORK_STATUS_CHOICES = [
        ('H1', 'H1'),
        ('OPT', 'OPT'),
        ('GC', 'Green Card'),
        ('USC', 'US Citizen'),
    ]

    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    access_level = models.CharField(
        max_length=10,
        choices=ACCESS_LEVEL_CHOICES
    )

    work_status = models.CharField(
        max_length=10,
        choices=WORK_STATUS_CHOICES
    )

    def __str__(self):
        return f"{self.employee_id} - {self.name}"
