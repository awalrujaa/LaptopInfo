from django.db import models
from django.core.exceptions import ValidationError


def validate_file_type(value):
    valid_extensions = ['jpg', 'png', 'jpeg']
    file_extension = value.name.split('.')[-1]
    
    if file_extension.lower() not in valid_extensions:
        raise ValidationError("Invalid file types. Only Images allowed.")
    

def validate_file_size(value):
    allowed_size = 2*1024*1024

    if value.size > allowed_size:
        raise ValidationError("File size exceeds allowed limit of 2 MB.")

# Create your models here.
class ComputerBrand(models.Model):
    brand_name = models.CharField(max_length=50)
    logo = models.FileField(validators=[validate_file_size, validate_file_type])


    def __str__(self):
        return self.brand_name

class ComputerSpecification(models.Model):
    generation = models.CharField(max_length=20)
    price_min = models.DecimalField(max_digits=9, decimal_places= 2)
    price_max = models.DecimalField(max_digits=11, decimal_places= 2)
    ram = models.IntegerField()
    brand = models.ForeignKey(ComputerBrand, on_delete=models.CASCADE)


    def __str__(self):
        return self.generation


class Computer(models.Model):
    image = models.FileField(validators=[validate_file_size, validate_file_type], upload_to="")
    computer_code = models.IntegerField(unique=True)
    specification = models.ForeignKey(ComputerSpecification, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_rate = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return str(self.computer_code)



