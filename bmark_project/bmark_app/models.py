from django.db import models

# Create your models here.
class Customer(models.Model):
    cus_id=models.AutoField(primary_key=True)
    cus_name=models.CharField(max_length=100)
    geo_lat=models.CharField(max_length=100,blank=True,null=True)
    geo_long=models.CharField(max_length=100,blank=True,null=True)


    def __int__(self):
        return self.cus_id

class Bookmark(models.Model):
    book_id=models.AutoField(primary_key=True)
    #Booking_date=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=200)
    url=models.URLField(max_length = 200)
    source_name=models.CharField(max_length=200)

    def __int__(self):
        return self.book_id


class CustomerBookmark(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete = models.CASCADE)
    bookmark_id = models.ForeignKey(Bookmark,on_delete = models.CASCADE)
    BookMark_date=models.DateTimeField(auto_now=True)
