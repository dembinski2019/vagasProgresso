# Generated by Django 3.0.5 on 2020-04-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200417_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='curriculum',
            field=models.FileField(default='', upload_to='', verbose_name='curriculo'),
        ),
    ]