# Generated by Django 4.2.2 on 2023-06-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0004_merge_20230611_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='updated_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
