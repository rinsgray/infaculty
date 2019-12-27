# Generated by Django 2.1.7 on 2019-12-06 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arithmetic', '0002_rule_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionWithSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QWS_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection_text', models.TextField()),
                ('selection_correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arithmetic.QuestionWithSelection')),
            ],
        ),
    ]
