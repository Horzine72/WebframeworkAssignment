
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text





class Customertable(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=128)
    Date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'customertable'


# used for {%%}
class Invoice(models.Model):
    invoice_id = models.AutoField(db_column='InvoiceID', primary_key=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices', db_column='CustomerID')
    amount = models.DecimalField(max_digits=10, decimal_places=2, db_column='Amount')
    parcel_detail = models.TextField(db_column='ParcelDetail')
    delivery_area = models.CharField(max_length=100, db_column='DeliveryArea')
    origin_country = models.CharField(max_length=100, db_column='OriginCountry')
    date = models.DateTimeField(default=now, editable=False, db_column='Date')

    class Meta:
        managed = False
        db_table = 'invoicetable'
        permissions = [
            ('can_add_invoice', 'Can Add Invoice'),
        ]