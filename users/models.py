from django.db import models

from users import constants as constants

# Create your models here.


class Contests(models.Model):
    platform = models.CharField(max_length=255, default='Codeforces')
    platform_id = models.BigIntegerField()
    contest_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    phase = models.CharField(max_length=255)
    frozen = models.BooleanField()
    duration_seconds = models.BigIntegerField()
    start_time = models.DateTimeField()
    notification_level = (
        (1, 'ADDED'),
        (2, 'BEFORE'),
        (3, 'Registration'),
        (4, 'CODING'),
        (5, 'PENDING_SYSTEM_TEST'),
        (6, 'SYSTEM_TEST'),
        (7, 'FINISHED')
    )

    @property
    def codeforces_contest_url(self):
        return constants.CODEFORCES_CONTEST_BASE_URL + self.platform_id

    class Meta:
        index_together = [['platform', 'platform_id']]


class Dictionary(models.Model):
    key = models.CharField(max_length=255, db_index=True)
    value = models.CharField(max_length=255)
