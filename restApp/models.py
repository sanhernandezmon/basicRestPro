from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
# Create your models here.
class Test(models.Model):
    intType = models.IntegerField(validators=[validate_even] )
    stringType = models.CharField(max_length=32, validators=[])
    boolType = models.BooleanField()

    class Meta:
        order_with_respect_to = 'intType'
