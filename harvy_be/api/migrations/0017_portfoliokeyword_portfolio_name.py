# Generated by Django 5.1.1 on 2024-10-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_portfoliofiles_file_path_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliokeyword',
            name='portfolio_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
