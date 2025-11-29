from django.db import models

# Create your models here.
class Sla_Report(models.Model):
    name = models.CharField(max_length=200)

    uptimeT = models.DecimalField(max_digits=7, decimal_places=3, default=0.0)
    uptime30 = models.DecimalField(max_digits=7, decimal_places=3)
    uptime90 = models.DecimalField(max_digits=7, decimal_places=3)
    uptime90d = models.DecimalField(max_digits=7, decimal_places=3, default=0.0)
    uptime365 = models.DecimalField(max_digits=7, decimal_places=3)
    """
    uptime30 = models.CharField(max_length=200)
    uptime90 = models.CharField(max_length=200)
    uptime365 = models.CharField(max_length=200)
    """

    group = models.CharField(max_length=200, default = 'NA')
    last_update = models.DateTimeField('date updated')
    class Meta:
        db_table = "sla_report"

    def __str__(self):
        return self.name