from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Words(models.Model):
    qid = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    stimulus_1 = models.CharField(max_length=20, blank=True, null=True)
    stimulus_2 = models.CharField(max_length=20, blank=True, null=True)
    stimulus_3 = models.CharField(max_length=20, blank=True, null=True)
    stimulus_4 = models.CharField(max_length=20, blank=True, null=True)
    stimulus_5 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'words'

