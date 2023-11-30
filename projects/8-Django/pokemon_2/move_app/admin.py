from django.contrib import admin

# Register your models here.
# move_app/admin
from .models import Move

admin.site.register([Move])
