# Generated by Django 5.1.4 on 2024-12-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_courtschedule_court_id_court_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='court',
            name='city',
            field=models.CharField(default='Cairo', max_length=100),
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
