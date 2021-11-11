from django.contrib import admin

# Register your models here.
from athena.account.models import User

admin.site.register(User)
