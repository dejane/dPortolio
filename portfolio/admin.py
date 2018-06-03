from django.contrib import admin

# Register your models here.

from .models import Portfolio, PortfolioInstance, Coin, CoinInstance

admin.site.register(Portfolio)
admin.site.register(PortfolioInstance)
admin.site.register(Coin)
admin.site.register(CoinInstance)
