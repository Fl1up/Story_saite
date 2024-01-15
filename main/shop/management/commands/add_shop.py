from django.core.management.base import BaseCommand

from main.shop.models import Shop


class Command(BaseCommand):
    def handle(self, *args, **options):
        Shop.objects.all().delete(),

        Shop.objects.create(
            name='Двери',
            price=1000,
            image="/icon/Без имени-4.png",
            description="Лучшие двери ")

        Shop.objects.create(
            name='Стены',
            price=200,
            image="/icon/Без имени-2.png",
            description="Лучшие стены ")

        Shop.objects.create(
            name='Кирпич',
            price=200,
            image="/icon/Без имени-3.png",
            description="Лучшие кирпичи ")
        Shop.objects.create(
            name='Двери',
            price=1000,
            image="/icon/Без имени-4.png",
            description="Лучшие двери ")

        Shop.objects.create(
            name='Стены',
            price=200,
            image="/icon/Без имени-2.png",
            description="Лучшие стены ")

        Shop.objects.create(
            name='Кирпич',
            price=200,
            image="/icon/Без имени-3.png",
            description="Лучшие кирпичи ")
        Shop.objects.create(
            name='Двери',
            price=1000,
            image="/icon/Без имени-4.png",
            description="Лучшие двери ")

        Shop.objects.create(
            name='Стены',
            price=200,
            image="/icon/Без имени-2.png",
            description="Лучшие стены ")

        Shop.objects.create(
            name='Кирпич',
            price=200,
            image="/icon/Без имени-3.png",
            description="Лучшие кирпичи ")
