from django.db import models

# Create your models here.
class CmAcct(models.Model):
    account = models.IntegerField(primary_key=True)
    exp_date = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'CM_ACCT'