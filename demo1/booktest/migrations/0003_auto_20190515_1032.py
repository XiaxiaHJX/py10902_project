# Generated by Django 2.2.1 on 2019-05-15 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20190515_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='gender',
            field=models.CharField(choices=[(1, '男'), (2, '女')], max_length=10, verbose_name='性别'),
        ),
    ]