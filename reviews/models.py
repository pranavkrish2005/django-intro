from django.db import models

class Review(models.Model):
    review_text = models.CharField(max_length=100, blank=True)
