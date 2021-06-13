# Generated by Django 3.0.8 on 2021-05-31 10:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=50, null=True)),
                ('l_name', models.CharField(max_length=50, null=True)),
                ('company_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50, null=True)),
                ('street_address', models.CharField(max_length=50, null=True)),
                ('town', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tbl_customers',
            },
        ),
        migrations.CreateModel(
            name='process',
            fields=[
                ('proc_id', models.AutoField(primary_key=True, serialize=False)),
                ('proc_code', models.CharField(max_length=100, unique=True)),
                ('proc_datetime', models.DateTimeField(max_length=100)),
                ('proc_qty', models.FloatField(max_length=100)),
                ('proc_type', models.CharField(max_length=100)),
                ('proc_stock', models.BigIntegerField()),
            ],
            options={
                'db_table': 'tbl_process',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_code', models.CharField(max_length=100)),
                ('prod_rate', models.FloatField(max_length=100)),
                ('prod_gst', models.FloatField(max_length=100)),
                ('prod_stock', models.BigIntegerField()),
            ],
            options={
                'db_table': 'tbl_products',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ord_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('ord_date', models.DateTimeField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('ord_price', models.FloatField(max_length=100)),
                ('ord_qty', models.BigIntegerField(max_length=100)),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.customer')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Products')),
            ],
            options={
                'db_table': 'tbl_order',
            },
        ),
    ]