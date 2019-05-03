from django.db import models
import datetime
from django.core.exceptions import ValidationError
# Create your models here.
def validate_image(value):
    print(value)
    if value.size > 10*1024*1024:
        raise ValidationError("Image file too large ( > 10mb )")
    else:
        return value


def image_path(instance, filename):
    return 'images/%s' % (filename)



class Images(models.Model):
    image = models.ImageField(upload_to=image_path,  validators=[validate_image])
    name = models.CharField(max_length=255, default="")
    date_in_database = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
    