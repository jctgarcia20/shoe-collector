# Generated by Django 4.0.4 on 2022-05-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('activity', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='shoe',
            name='occasions',
            field=models.ManyToManyField(to='main_app.occasion'),
        ),
    ]