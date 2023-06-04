# Generated by Django 4.2 on 2023-05-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=150)),
                ('batafsil', models.TextField()),
                ('holat', models.CharField(choices=[('Yangi', 'Yangi'), ('Bajarilyapti', 'Bajarilyapti'), ('Bajarildi', 'Bajarildi')], max_length=20)),
                ('sana', models.DateField()),
            ],
        ),
    ]