from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

class CmAcct(models.Model):
    account = models.IntegerField(db_column='Account', primary_key=True)  # Field name made lowercase.
    cm_name = models.CharField(db_column='CM_Name', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    cm_mobile = models.CharField(db_column='CM_mobile', max_length=1, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CM_ACCT'

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE
