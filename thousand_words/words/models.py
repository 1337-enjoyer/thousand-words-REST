from django.db import models


class Words(models.Model):
    word = models.CharField()
    translation = models.CharField()

    class Meta:
        managed = False
        db_table = 'words'
