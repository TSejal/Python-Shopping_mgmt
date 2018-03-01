# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('category', models.CharField(max_length=50, null=True, blank=True)),
                ('quantity', models.PositiveIntegerField(null=True, blank=True)),
                ('unit_sold', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('price', models.DecimalField(max_digits=16, decimal_places=2)),
                ('publish_status', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=255, null=True, blank=True)),
                ('website', models.URLField(null=True, verbose_name=b'Store Website', blank=True)),
                ('enabled', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name=b'email address')),
                ('first_name', models.CharField(max_length=255, verbose_name=b'first name', blank=True)),
                ('last_name', models.CharField(max_length=255, verbose_name=b'last name', blank=True)),
                ('avatar', models.ImageField(upload_to=b'avatar/')),
                ('country', models.CharField(max_length=255, verbose_name=b'Country')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'active')),
                ('date_joined', models.DateTimeField(verbose_name=b'date joined')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='seller',
            name='profile',
            field=models.OneToOneField(related_name=b'user_seller_profile', to='Shopping_models.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='added_by',
            field=models.ForeignKey(related_name=b'added_products', to='Shopping_models.User'),
            preserve_default=True,
        ),
    ]
