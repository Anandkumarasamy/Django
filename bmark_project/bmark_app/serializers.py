from rest_framework import serializers
from bmark_app.models import Customer,Bookmark,CustomerBookmark

class Customer_serializer(serializers.ModelSerializer):

    class Meta:
        model=Customer
        #fields = ('cus_id','cus_name','geo_lat','geo_long')
        fields = '__all__'

class Bookmark_serializer(serializers.ModelSerializer):

    class Meta:
        model=Bookmark
        #fields = ('book_id','Booking_date','title','url','source_name')
        fields = ('title','source_name')
        #fields = '__all__'

class CustomerBookmark_serializer(serializers.ModelSerializer):

    class Meta:
        model=CustomerBookmark
        #fields = ('customer_id','bookmark_id','BookMark_date')
        fields = ('BookMark_date')
        #fields = '__all__'
