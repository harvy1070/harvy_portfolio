# Generated by Django 5.1.1 on 2024-09-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_pjtimeline_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='pjtimeline',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='소속 회사'),
        ),
    ]
