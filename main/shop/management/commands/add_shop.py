from django.core.management.base import BaseCommand

from main.shop.models import Shop


class Command(BaseCommand):
    def handle(self, *args, **options):
        Shop.objects.all().delete(),

        Shop.objects.create(
            name='Двери',
            price=1000,
            image="img_21.png",
            description="Лучшие двери ")

        Shop.objects.create(
            name='Стены',
            price=200,
            image="img_23.png",
            description="Лучшие стены ")

        Shop.objects.create(
            name='Кирпич',
            price=200,
            image="img_20.png",
            description="Лучшие кирпичи ")

        Shop.objects.create(
            name='Окна',
            price=200,
            image="img_19.png",
            description="Лучшие окна ")

        Shop.objects.create(
            name='Кирпич',
            price=200,
            image="img_20.png",
            description="Лучшие кирпичи ")

        Shop.objects.create(
            name='Окна',
            price=200,
            image="img_19.png",
            description="Лучшие окна ")

        Shop.objects.create(
            name='Двери',
            price=1000,
            image="img_21.png",
            description="Лучшие двери ")

        Shop.objects.create(
            name='Стены',
            price=200,
            image="img_23.png",
            description="Лучшие стены ")

        Shop.objects.create(
            name='Кирпич',
            price=200,
            image="img_20.png",
            description="Лучшие кирпичи ")

        Shop.objects.create(
            name='Окна',
            price=200,
            image="img_19.png",
            description="Лучшие окна ")

        Shop.objects.create(
            name='Кирпич',
            price=200,
            image="img_20.png",
            description="Лучшие кирпичи ")

        Shop.objects.create(
            name='Окна',
            price=200,
            image="img_19.png",
            description="Лучшие окна ")
