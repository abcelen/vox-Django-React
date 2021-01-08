# Generated by Django 2.2.2 on 2019-06-11 03:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_type', models.CharField(choices=[('m', 'Monthly'), ('o', 'One Time Order')], help_text='Package Type', max_length=1)),
                ('quantity', models.PositiveIntegerField(help_text='Narrations Ordered')),
                ('list_all_posts', models.BooleanField(default=False, help_text='List posts in the VoxSnap Library')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('stripe_id', models.CharField(blank=True, max_length=512, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True)),
                ('stripe_coupon_id', models.CharField(max_length=128)),
                ('max_usages', models.IntegerField(blank=True, null=True)),
                ('discount_fixed', models.PositiveIntegerField(blank=True, null=True)),
                ('discount_percent', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('expiration_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]