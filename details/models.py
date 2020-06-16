from django.db import models


class ApiView(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_age = models.IntegerField(null=True)
    stu_class = models.IntegerField(null=True)
    stu_location = models.CharField(max_length=20,null=True)
    stu_gender = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.stu_name