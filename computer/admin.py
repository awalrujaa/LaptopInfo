from django.contrib import admin
from .models import ComputerBrand, ComputerSpecification, Computer

# Register your models here.
admin.site.register(ComputerBrand)
admin.site.register(ComputerSpecification)
admin.site.register(Computer)

# @admin.register(ComputerBrand)
# class ComputerBrandAdmin(admin.ModelAdmin):
#     list_display = ('brand_name', 'logo')

