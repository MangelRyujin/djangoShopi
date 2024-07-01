from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext_lazy as _

def validate_phone_number(value):
   if not re.match(r'^\+?[1-9][0-9]{7,14}$', value):
        raise ValidationError(
            _("Invalid phone number")
        )