# Generated by Django 5.1.3 on 2024-12-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
