from django.shortcuts import render
from .models import Coin, CoinInstance, Portfolio


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Portfolio.objects.all().count()
    num_instances = CoinInstance.objects.all().count()


    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances },
    )