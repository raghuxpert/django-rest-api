from django.db import models

# Create your models here.
class CmDvceDsgn(models.Model):
    dsgn_cde = models.IntegerField(db_column='Dsgn_cde', primary_key=True)  # Field name made lowercase.
    dsgn_exp_date = models.DateField()
    design_desc = models.TextField()
    material_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'CM_DVCE_DSGN'