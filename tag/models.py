from django.db import models
from resource.models import Resource
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    class Meta:
        db_table = "tag"