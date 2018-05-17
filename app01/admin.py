from django.contrib import admin
from app01.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
