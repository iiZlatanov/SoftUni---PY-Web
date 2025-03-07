from django.db import models


class Employee(models.Model):
    MAX_FIRST_NAME_LENGTH = 35
    ROLES = (
        (1, 'Software Developer'),
        (2, 'QA engineer'),
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
    )

    role = models.IntegerField(
        choices=ROLES,
    )
