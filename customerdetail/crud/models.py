
from django.db import models  
class Employee(models.Model):  
    cid = models.CharField(max_length=20)  
    cname = models.CharField(max_length=100)  
    cemail = models.EmailField()  
    ccontact = models.IntegerField(max_length=15) 

    def __str__(self):
        return "%s " %(self.cname) 
    class Meta:  
        db_table = "customer"