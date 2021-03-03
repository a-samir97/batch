# Generated by Django 3.1.7 on 2021-03-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X Large')], default='S', max_length=2)),
                ('color', models.CharField(choices=[('R', 'Red'), ('BE', 'Blue'), ('BK', 'Black'), ('G', 'Green')], default='R', max_length=2)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]