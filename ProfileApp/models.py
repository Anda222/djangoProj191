from django.db import models

class Product(models.Model):
    #ขายเมาส์ปากกา
    id = models.CharField(max_length=5,default='',primary_key=True)
    brand = models.CharField(max_length=100,default='')
    model = models.CharField(max_length=100,default='')
    screen = models.CharField(max_length=100,default='')
    size = models.CharField(max_length=100,default='')
    pressure = models.CharField(max_length=100,default='')
    weight = models.CharField(max_length=100,default='')
    price = models.FloatField(max_length=100,default='')
    amount = models.IntegerField(max_length=100,default='')

    def pSum(self):
        sum = self.price*self.amount
        return sum

    def pDiscount(self):
        if self.pSum() < 1500:
            discount = self.pSum() * 5 / 100
        elif self.pSum() < 3000:
            discount = self.pSum() * 7 / 100
        else:
            discount = self.pSum() * 10 / 100
        return discount

    def pTotal(self):
        total = self.pSum() - self.pDiscount()
        return total