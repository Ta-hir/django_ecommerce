from django.contrib import admin
from .models import Category,Customer,Product,Order,Profile
from django.contrib.auth.models import User 
# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


# mix profile infoand user info

class ProfileInline(admin.StackedInline):
    model =Profile

# extend the user model
class userAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]

# inregister the oldway
admin.site.unregister(User)

# register new way
admin.site.register(User, userAdmin)