# Generated by Django 4.0.5 on 2022-06-05 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.author'),
            preserve_default=False,
        ),
    ]
