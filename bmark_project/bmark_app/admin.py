from django.contrib import admin
from bmark_app.models import Customer,Bookmark,CustomerBookmark
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['cus_id','cus_name','geo_lat','geo_long']

admin.site.register(Customer,CustomerAdmin)

class BookmarkAdmin(admin.ModelAdmin):
    list_display=['book_id','title','url','source_name']

admin.site.register(Bookmark,BookmarkAdmin)

class CustomerBookmarkAdmin(admin.ModelAdmin):
    list_display=['customer_id','bookmark_id','BookMark_date']

admin.site.register(CustomerBookmark,CustomerBookmarkAdmin)
