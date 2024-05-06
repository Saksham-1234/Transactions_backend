from django.db import models
#Database Setup
class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    invoice_url = models.URLField()

    def __str__(self):
        return self.transaction_id