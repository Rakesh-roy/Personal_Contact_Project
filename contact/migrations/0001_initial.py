# Generated by Django 3.0.5 on 2021-01-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Friends', 'Friends'), ('Family', 'Family'), ('Office', 'Office'), ('Faculty', 'Faculty')], max_length=100)),
            ],
        ),
    ]