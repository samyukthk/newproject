from django.contrib import admin
from djangoapp.models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ImageTest)
admin.site.register(ProductVariant)