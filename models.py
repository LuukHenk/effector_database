""" Database models """
from django.db import models

class Sequence(models.Model):
    """ Information about an effector ID it's sequence """
    effector_id = models.CharField(max_length=200, primary_key=True)
    effector_sequence = models.TextField()

    def __str__(self):
        return self.effector_id
