# Generated by Django 5.0 on 2023-12-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=150)),
                ('transaction_date', models.DateField()),
                ('due_date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Due', 'Due'), ('Canceled', 'Canceled')], max_length=20)),
            ],
        ),
    ]
