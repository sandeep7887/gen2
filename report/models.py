from django.db import models

# Create your models here.


class execution_details(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    project = models.CharField(max_length=100)
    test_type = models.CharField(max_length=20)
    execution_date = models.DateField()

class execution_summary(models.Model):
    tcname = models.CharField(max_length=150)
    suite = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    reference_id = models.ForeignKey(execution_details,on_delete=models.CASCADE)