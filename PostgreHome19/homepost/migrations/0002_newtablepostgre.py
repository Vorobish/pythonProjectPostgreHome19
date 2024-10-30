# Generated by Django 5.1.2 on 2024-10-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTablePostgre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('discription', models.TextField()),
                ('price', models.DecimalField(decimal_places=6, max_digits=20)),
            ],
        ),
    ]