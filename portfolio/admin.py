from django.contrib import admin

# Register your models here.

from .models import Portfolio, Coin, CoinInstance

admin.site.register(Portfolio)
admin.site.register(Coin)
admin.site.register(CoinInstance)
