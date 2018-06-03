from django.db import models
import uuid  # Required for unique portfolio instances


# coin and coin instances

class Coin(models.Model):

    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    priceUSD = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coin-detail', args=[str(self.id)])



class CoinInstance(models.Model):

        id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                              help_text="Unique ID for this particular coin instance")

        coin = models.ForeignKey('Coin', on_delete=models.SET_NULL, null=True)
        quantity = models.CharField(max_length=200)
        value = models.CharField(max_length=200)

        def __str__(self):

            return '{0} ({1})'.format(self.id, self.coin.name)


# Portfolios and instances

class Portfolio(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])



class PortfolioInstance(models.Model):

        id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                              help_text="Unique ID for this particular portfolio")
        portfolio = models.ForeignKey('Portfolio', on_delete=models.SET_NULL, null=True)
        value = models.CharField(max_length=200)

        coins = models.ManyToManyField(CoinInstance, help_text='Select a coins for this portfolio')

        def __str__(self):

            return '{0} ({1})'.format(self.id, self.portfolio.title)


