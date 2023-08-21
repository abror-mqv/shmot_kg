from django.db import models
from colorfield.fields import ColorField


class Category(models.Model):
    cat_name = models.CharField(verbose_name='Категория', max_length=127)

    def __str__(self):
        return self.cat_name


class SubCategory(models.Model):
    subcat_name = models.CharField(verbose_name='Подкатегория', max_length=127)
    father = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.father.cat_name} -> {self.subcat_name}"


class SubSubCategory(models.Model):
    subsubcat_name = models.CharField(
        verbose_name='Подподкатегория', max_length=127)
    father = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.father.father.cat_name} -> {self.father.subcat_name} -> {self.subsubcat_name}"


class Product(models.Model):
    product_name = models.CharField(verbose_name='Товар', max_length=127)
    # image = models.ImageField(verbose_name='Previous image', default=None, null=True, blank=True)
    image_0 = models.ImageField(
        verbose_name="Изображение 0", default=None, null=True, blank=True)
    color_name_0 = models.CharField(max_length=63,
                                    verbose_name='Название цвета 0', null=True, blank=True, default=None)
    color_0 = ColorField(default='#FFFFFF', null=True, blank=True)

    image_1 = models.ImageField(
        verbose_name="Изображение 1", default=None, null=True, blank=True)
    color_name_1 = models.CharField(max_length=63,
                                    verbose_name='Название цвета 1', null=True, blank=True, default=None)
    color_1 = ColorField(default='#FFFFFF', null=True, blank=True)

    image_2 = models.ImageField(
        verbose_name="Изображение 2", default=None, null=True, blank=True)
    color_name_2 = models.CharField(max_length=63,
                                    verbose_name='Название цвета 2', null=True, blank=True, default=None)
    color_2 = ColorField(default='#FFFFFF', null=True, blank=True)

    image_3 = models.ImageField(
        verbose_name="Изображение 3", default=None, null=True, blank=True)
    color_name_3 = models.CharField(max_length=63,
                                    verbose_name='Название цвета 3', null=True, blank=True, default=None)
    color_3 = ColorField(default='#FFFFFF', null=True, blank=True)

    image_4 = models.ImageField(
        verbose_name="Изображение 4", default=None, null=True, blank=True)
    color_name_4 = models.CharField(max_length=63,
                                    verbose_name='Название цвета 4', null=True, blank=True, default=None)
    color_4 = ColorField(default='#FFFFFF', null=True, blank=True)

    siezes = models.CharField(
        verbose_name='Размеры', default=None, max_length=63, null=True, blank=True)
    repeat_size = models.CharField(
        verbose_name='Повторный размер', default=None, max_length=63, null=True, blank=True)
    description = models.TextField(
        verbose_name="Описание", max_length=255, default=None)
    price = models.PositiveBigIntegerField()
    father = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE)
    location = models.CharField(
        verbose_name='Локация товара', max_length=127, default=None, null=True, blank=True)
    seller = models.CharField(verbose_name='Продавец',
                              max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.father.subsubcat_name} - {self.product_name}"


class Customer(models.Model):
    PRODUCT_TYPES = [
        ('that_base_fr', 'БДФР'),
        ('that_base_ot', 'БДДР'),
        ('insta_direct_search', 'Инста, прямой поиск'),
        ('insta_target', 'Инста, таргет'),
        ('sarafan', 'Сарафан'),
    ]
    name = models.CharField(verbose_name='Имя клиента', max_length=127)
    number = models.CharField(
        verbose_name='Номер телефона', max_length=30, blank=True, null=True)
    is_wa = models.BooleanField(
        verbose_name='есть Вотсап?', blank=True, null=True)
    telegram_username = models.CharField(
        verbose_name='Юзернейм ТГ', max_length=127, blank=True, null=True)
    telegram_id = models.CharField(
        verbose_name='Айди ТГ', max_length=20, blank=True, null=True)
    telegram_number = models.CharField(
        verbose_name='Номер тг', max_length=127, blank=True, null=True)
    description = models.TextField(
        verbose_name='Доп сведения', blank=True, null=True)
    origins = models.CharField(verbose_name='Как я встретил вашу маму',
                               choices=PRODUCT_TYPES, max_length=127, blank=True, null=True)
    city_from = models.CharField(
        verbose_name='Город', max_length=127, blank=True, null=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Корзина {self.user.name}: {self.quantity} x {self.product.product_name}"


class Market(models.Model):
    name = models.CharField(verbose_name='Рынок', max_length=127)
    def __str__(self):
        return f"Рынок: {self.name}"
    
