# Generated by Django 4.0.4 on 2022-07-13 08:24

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_post_comment_count_alter_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 7, 13, 8, 24, 10, 8795, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='replypostcomment',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Updated_at'),
        ),
    ]
