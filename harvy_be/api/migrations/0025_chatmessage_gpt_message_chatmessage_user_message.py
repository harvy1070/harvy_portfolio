# Generated by Django 5.1.1 on 2024-10-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_rename_api_chatmes_user_id_ee15fd_idx_chatmessage_user_id_27a1be_idx_and_more'),
    ]

    operations = [
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
