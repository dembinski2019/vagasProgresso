# Generated by Django 3.0.5 on 2020-04-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200417_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='curriculum',
            field=models.FileField(upload_to='candidate/curriculum', verbose_name='Curriculo'),
        ),
    ]