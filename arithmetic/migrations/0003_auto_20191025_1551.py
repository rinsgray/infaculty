# Generated by Django 2.1.7 on 2019-10-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arithmetic', '0002_auto_20191025_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='rule_text',
            field=models.TextField(),
        ),
    ]
