# Generated by Django 3.2.5 on 2023-06-14 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0005_alter_menuitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='LittleLemonDRF.order'),
        ),
    ]
