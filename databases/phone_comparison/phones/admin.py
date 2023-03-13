from django.contrib import admin

# Register your models here.
@admin.register(models.Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','image','release_date','lte_exists','slug')

admin.site.register(models.Phone, PhoneAdmin)