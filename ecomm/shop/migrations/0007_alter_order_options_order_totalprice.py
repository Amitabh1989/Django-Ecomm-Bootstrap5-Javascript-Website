# Generated by Django 4.2.1 on 2023-06-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_alter_order_zipcode"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": [
                    "name",
                    "email",
                    "address",
                    "city",
                    "zipcode",
                    "state",
                    "items",
                    "totalPrice",
                ]
            },
        ),
        migrations.AddField(
            model_name="order",
            name="totalPrice",
            field=models.CharField(default=10000, max_length=200),
            preserve_default=False,
        ),
    ]