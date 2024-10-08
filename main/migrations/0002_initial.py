# Generated by Django 4.2.6 on 2024-09-10 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='avtor'),
        ),
        migrations.AddField(
            model_name='test',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='kategoriya'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.test'),
        ),
        migrations.AddField(
            model_name='checktest',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='checktest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checktests', to='main.test'),
        ),
        migrations.AddField(
            model_name='checkquestion',
            name='checktest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.checktest'),
        ),
        migrations.AddField(
            model_name='checkquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question'),
        ),
    ]
