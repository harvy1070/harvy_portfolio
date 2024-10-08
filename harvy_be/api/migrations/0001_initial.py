# Generated by Django 5.1.1 on 2024-09-07 09:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PjTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('career', '경력'), ('project', '프로젝트')], max_length=20, verbose_name='항목 유형')),
                ('title', models.CharField(max_length=100, verbose_name='프로젝트 명')),
                ('description', models.TextField(blank=True, null=True, verbose_name='설명')),
                ('date', models.DateField(verbose_name='날짜')),
                ('order_num', models.IntegerField(blank=True, null=True, verbose_name='표시 순서')),
            ],
            options={
                'ordering': ['order_num', '-date'],
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='유저이름')),
                ('user_email', models.EmailField(max_length=254, unique=True, verbose_name='이메일')),
                ('user_tel1', models.CharField(blank=True, max_length=20, null=True, verbose_name='유선번호')),
                ('user_tel2', models.CharField(max_length=20, verbose_name='무선번호(핸드폰)')),
                ('user_addr1', models.CharField(blank=True, max_length=50, null=True, verbose_name='주소')),
                ('user_addr2', models.CharField(blank=True, max_length=50, null=True, verbose_name='세부주소')),
                ('user_corpname', models.CharField(max_length=20, verbose_name='소속회사')),
                ('user_corpdept', models.CharField(max_length=20, verbose_name='소속부서')),
                ('user_corptype', models.CharField(max_length=20, verbose_name='회사유형')),
                ('user_signin', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자들',
            },
        ),
        migrations.CreateModel(
            name='PortfolioBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='유저이름')),
                ('board_title', models.TextField(verbose_name='글 제목')),
                ('board_desc', models.TextField(blank=True, null=True, verbose_name='글 내용')),
                ('board_write', models.DateTimeField(auto_now_add=True, verbose_name='글 작성일')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255, verbose_name='업로드된 파일 이름')),
                ('file_path', models.CharField(max_length=255, verbose_name='파일 저장 경로')),
                ('file_size', models.IntegerField(blank=True, null=True, verbose_name='파일 크기 (바이트)')),
                ('file_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='파일 MIME 타입')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='파일 업로드 일시')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.portfolioboard')),
            ],
        ),
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.TextField(verbose_name='질문 제목')),
                ('question_desc', models.TextField(verbose_name='질문 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='질문 작성일')),
                ('answer_title', models.TextField(blank=True, null=True, verbose_name='답변 제목')),
                ('answer_desc', models.TextField(blank=True, null=True, verbose_name='답변 내용')),
                ('answered_at', models.DateTimeField(blank=True, null=True, verbose_name='답변 작성일')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qnas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
