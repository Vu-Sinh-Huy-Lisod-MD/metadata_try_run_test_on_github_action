from django.db import models

# Create your models here.
class TypeSource(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "type_resource"