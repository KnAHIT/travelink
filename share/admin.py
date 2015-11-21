from django.contrib import admin
from share.models import Account, Blog,Diary
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Username',)
    search_fields = ('Username',)
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('Title',)

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('Title',)

admin.site.register(Account,AccountAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Diary,DiaryAdmin)
