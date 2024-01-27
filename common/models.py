from django.db import models

class DatesTimeModel(models.Model):
    """
    Stores created_at and updated_at fields for all models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
