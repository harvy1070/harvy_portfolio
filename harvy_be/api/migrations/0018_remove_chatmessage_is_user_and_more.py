# Generated by Django 5.1.1 on 2024-10-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_portfoliokeyword_portfolio_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='is_user',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='message',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='gpt_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='user_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
