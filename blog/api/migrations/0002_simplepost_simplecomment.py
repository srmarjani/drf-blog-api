# Generated by Django 4.2 on 2024-07-18 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SimplePost",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(blank=True, default="", max_length=100)),
                ("body", models.TextField(blank=True, default="")),
            ],
            options={
                "ordering": ["created"],
            },
        ),
        migrations.CreateModel(
            name="SimpleComment",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("body", models.TextField()),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="api.simplepost",
                    ),
                ),
            ],
            options={
                "ordering": ["created"],
            },
        ),
    ]
