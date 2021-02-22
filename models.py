""" Database models """
from django.db import models

class Sequence(models.Model):
    """ Information about an effector ID it's sequence """
    effector_id = models.CharField(
        max_length=200,
        primary_key=True,
        unique=True
    )
    effector_sequence = models.TextField(max_length=10.000)
    effector_name = models.CharField(max_length=200, null=True)
    effector_description = models.TextField(max_length=2.000, null=True)
    effector_signal_peptide = models.BooleanField(default=False)

    def __str__(self):
        return self.effector_id

class Species(models.Model):
    species = models.CharField(max_length=200, primary_key=True, unique=True)
    isolate = models.CharField(max_length=200)
    interaction_partner = models.CharField(max_length=200)

    def __str__(self):
        return self.species
