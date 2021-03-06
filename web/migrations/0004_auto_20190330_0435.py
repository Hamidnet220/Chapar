# Generated by Django 2.1.7 on 2019-03-30 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0003_auto_20190330_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, validators=[web.models.empty_validate_event])),
                ('tel', models.CharField(blank=True, max_length=19)),
                ('fax', models.CharField(blank=True, max_length=19)),
                ('is_deleted', models.BooleanField(default=False)),
                ('add_by_usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_by_usr_org', to=settings.AUTH_USER_MODEL)),
                ('del_by_usr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='del_by_usr_org', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recive',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Organization'),
        ),
        migrations.AddField(
            model_name='send',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Organization'),
        ),
    ]
