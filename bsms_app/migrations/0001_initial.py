# Generated by Django 4.2.5 on 2023-10-11 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('book_photo', models.ImageField(blank=True, null=True, upload_to='nook_photo')),
                ('author_photo', models.ImageField(blank=True, null=True, upload_to='author_photo')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('rental_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rental_period', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('available', 'available'), ('rental', 'rental'), ('sold', 'sold')], max_length=50, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book_category', to='bsms_app.category')),
            ],
        ),
    ]
