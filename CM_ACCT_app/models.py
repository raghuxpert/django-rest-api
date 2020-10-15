from django.db import models
from datetime import datetime

# Create your models here.
class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

# Create your models here.
class CmAcct(models.Model):
    account = models.IntegerField(primary_key=True)
    exp_date = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'CM_ACCT'