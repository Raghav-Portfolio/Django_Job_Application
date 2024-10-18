from django.db import models


class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField(null=False)
    occupation = models.CharField(max_length=80)
    
    def __str__(self): # this magic function defines what should be printed in case a print(class_object) 
                       # is called somewhere in the code later
        return f'{self.first_name} {self.last_name}'
    
