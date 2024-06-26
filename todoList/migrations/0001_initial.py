# Generated by Django 4.2.13 on 2024-05-31 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="listItems",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dateCreated", models.DateField()),
                ("taskText", models.CharField(max_length=200)),
                ("finishedAt", models.DateTimeField()),
                (
                    "listName",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todoList.listitems",
                    ),
                ),
            ],
        ),
    ]
