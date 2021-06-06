from django.contrib import admin
from .models import Game


# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('Name', 'price', 'Popular')


admin.site.register(Game, GameAdmin)
