# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# from CM_DVCE_DSGN_app.models import CmDvceDsgn


class CmDvceInvtr(models.Model):
    account = models.IntegerField()
    seq_nbr = models.IntegerField()
    cm_name = models.TextField(db_column='CM_name')  # Field name made lowercase. This field type is a guess.
    cm_type = models.TextField(db_column='CM_type')  # Field name made lowercase. This field type is a guess.
    # cmdvcedsgn = models.ForeignKey(CmDvceDsgn, on_delete=models.CASCADE)
    design_cde = models.IntegerField()
    exp_date = models.IntegerField()
    emer_ind = models.CharField(max_length=1)
    cm_rrc = models.CharField(max_length=1)
    cm_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'CM_DVCE_INVTR'
        unique_together = (('account', 'seq_nbr'),)
