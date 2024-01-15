from django.shortcuts import render
from django.core.mail import send_mail
from main.shop.forms import ContactForm, CalculationForm
from main.shop.models import Shop
from django.views.generic import ListView


# Create your views here.
def main(request):
    shops = Shop.objects.all()

    context = {
        "shops": shops,

    }
    return render(request, "main_list.html", context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            message = request.POST.get('message')

            # Отправка письма
            send_mail(
                'Клиент',
                f'Имя: {name}\nEmail: {email}\nНомер: {number}\nСообщение: {message}',
                "margoonavt@yandex.ru",
                ['margoonavt@yandex.ru'],
                fail_silently=False,
            )

            return render(request, "main_list.html")

    else:
        form = ContactForm()

    return render(request, 'front/contact.html', {'form': form})


# def calculate_cost(request):  #калькулятор
#     if request.method == 'POST':
#         form = CalculationForm(request.POST)
#         if form.is_valid():
#             service = form.cleaned_data['service']
#             quantity = form.cleaned_data['quantity']
#             total_cost = service.price * quantity
#             return render(request, 'front/main_calculation.html', {'form': form, 'total_cost': total_cost})
#     else:
#         form = CalculationForm()
#     return render(request, 'front/main_calculation.html', {'form': form})


class ShopListView(ListView):
    model = Shop
    template_name = "front/shop_list.html"
