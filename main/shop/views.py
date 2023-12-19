from django.shortcuts import render

from main.shop.models import Shop


# Create your views here.
def main(request):
    shop = Shop.objects.all()

    context = {
        "shop": shop,

    }
    return render(request, "main_list.html", context)
