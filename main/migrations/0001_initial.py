# Generated by Django 4.2.3 on 2023-08-17 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=127, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Имя клиента')),
                ('number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер телефона')),
                ('is_wa', models.BooleanField(blank=True, null=True, verbose_name='есть Вотсап?')),
                ('telegram_username', models.CharField(blank=True, max_length=127, null=True, verbose_name='Юзернейм ТГ')),
                ('telegram_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='Айди ТГ')),
                ('telegram_number', models.CharField(blank=True, max_length=127, null=True, verbose_name='Номер тг')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Доп сведения')),
                ('origins', models.CharField(blank=True, choices=[('that_base_fr', 'БДФР'), ('that_base_ot', 'БДДР'), ('insta_direct_search', 'Инста, прямой поиск'), ('insta_target', 'Инста, таргет'), ('sarafan', 'Сарафан')], max_length=127, null=True, verbose_name='Как я встретил вашу маму')),
                ('city_from', models.CharField(blank=True, max_length=127, null=True, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat_name', models.CharField(max_length=127, verbose_name='Подкатегория')),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsubcat_name', models.CharField(max_length=127, verbose_name='Подподкатегория')),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=127, verbose_name='Товар')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Previous image')),
                ('siezes', models.CharField(blank=True, default=None, max_length=63, null=True, verbose_name='Размеры')),
                ('repeat_size', models.CharField(blank=True, default=None, max_length=63, null=True, verbose_name='Повторный размер')),
                ('description', models.TextField(default=None, max_length=255, verbose_name='Описание')),
                ('price', models.PositiveBigIntegerField()),
                ('location', models.CharField(blank=True, default=None, max_length=127, null=True, verbose_name='Локация товара')),
                ('seller', models.CharField(blank=True, max_length=255, null=True, verbose_name='Продавец')),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subsubcategory')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
            ],
        ),
    ]
