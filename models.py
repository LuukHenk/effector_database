""" Database models """
from django.db import models

class Sequence(models.Model):
    """ Information about an effector ID it's sequence """
    effector_id = models.CharField(
        max_length=150,
        primary_key=True,
        unique=True
    )
    effector_sequence = models.TextField(
        max_length=10000
    )
    effector_name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    effector_description = models.TextField(
        max_length=2000,
        blank=True,
        null=True
    )
    effector_signal_peptide = models.CharField(
        max_length=1,
        choices=[("T", "True"), ("F", "False"), ("", "")],
        default="",
        blank=True
    )

    def __str__(self):
        return self.effector_id

class Species(models.Model):
    species = models.CharField(max_length=200, primary_key=True, unique=True)
    isolate = models.CharField(max_length=200)
    interaction_partner = models.CharField(max_length=200)

    def __str__(self):
        return self.species
