# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Statement(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=255)
    search_text = models.CharField(max_length=255, default='', null=False)
    conversation = models.CharField(max_length=32, default='', null=False)
    created_at = models.DateTimeField()
    in_response_to = models.CharField(max_length=255, default='', null=False)
    search_in_response_to = models.CharField(max_length=255, default='', null=False)
    persona = models.CharField(max_length=50, default='', null=False)

    class Meta:
        db_table = 'statement'


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'tag'


class TagAssociation(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'tag_association'
