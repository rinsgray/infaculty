# Generated by Django 2.1.7 on 2019-12-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arithmetic', '0003_questionwithselection_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionwithselection',
            name='QWS_text',
            field=models.TextField(default='0'),
            preserve_default=False,
        ),
    ]
