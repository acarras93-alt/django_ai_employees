from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0005_rename_create_at_order_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order", name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="refundrequest", name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
