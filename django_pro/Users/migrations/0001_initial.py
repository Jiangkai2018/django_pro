# Generated by Django 2.1.3 on 2018-12-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('realname', models.CharField(max_length=255, verbose_name='真实姓名')),
                ('sex', models.CharField(max_length=10, verbose_name='性别')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='电子 邮箱')),
            ],
        ),
    ]
