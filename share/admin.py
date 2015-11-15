from django.contrib import admin
from share.models import Account, Blog
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Username',)
    search_fields = ('Username',)
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('Title',)
    

admin.site.register(Account,AccountAdmin)
admin.site.register(Blog,BlogAdmin)