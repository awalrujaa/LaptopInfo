from rest_framework import serializers
from .models import Computer

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ('computer_code', 'computer', 'quantity', 'unit_rate', 'total_price')


    #      computer_code = models.IntegerField(unique=True)
    # computer = models.ForeignKey(ComputerSpecification, on_delete=models.CASCADE)
    # quantity = models.IntegerField()
    # unit_rate = models.IntegerField()
    # total_price = models.IntegerField()
