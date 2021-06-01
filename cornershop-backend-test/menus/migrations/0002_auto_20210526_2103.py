# Generated by Django 3.0.8 on 2021-05-26 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customization', models.TextField(null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
                ('menu_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.MenuOption')),
            ],
        ),
        migrations.AddField(
            model_name='menuoption',
            name='employees',
            field=models.ManyToManyField(through='menus.EmployeeSelection', to='employees.Employee'),
        ),
    ]
