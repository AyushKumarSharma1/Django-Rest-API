from django.db import models

# Create your models here.
class CompanyDataSet(models.Model):
    companyId=models.IntegerField(auto_created=True)
    name=models.CharField(max_length=10)
    location=models.CharField(max_length=100)
    dateOfCreation=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return super().__str__()