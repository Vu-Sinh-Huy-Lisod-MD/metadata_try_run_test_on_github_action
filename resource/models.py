from pydoc import describe
from django.db import models
from type_resource.models import TypeSource

# Create your models here.
class Resource(models.Model):
    name = models.CharField(max_length=200)
    describe = models.CharField(max_length=500)
    type_resource = models.ForeignKey(TypeSource, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "resource"