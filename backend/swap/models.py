# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid
from django.db import models



class Faces(models.Model):
    fid = models.AutoField(db_column='FID', primary_key=True)  # Field name made lowercase.
    kid = models.ForeignKey('Knownface', models.DO_NOTHING, db_column='KID', blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FACES'


class Knownface(models.Model):
    kid = models.AutoField(db_column='KID', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='UID', blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FNAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KNOWNFACE'


class User(models.Model):
    uid = models.UUIDField(db_column='UID', primary_key=True, default=uuid.uuid4, editable=False)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='DOMAIN', max_length=20, blank=True, null=True)# Field name made lowercase.
    blur = models.CharField(db_column='BLUR', max_length=20, blank=True, null=True)# Field name made lowercase.
    pixel = models.CharField(db_column='PIXEL', max_length=20, blank=True, null=True)# Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'USER'
