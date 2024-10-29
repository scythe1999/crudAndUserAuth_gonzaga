from django.db import models

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    section = models.CharField(max_length=200, null=True, blank=True)
    studentid = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"