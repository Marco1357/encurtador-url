# Generated by Django 3.2.3 on 2021-05-20 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encurtador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('origem', models.URLField(blank=True, max_length=512, null=True)),
                ('user_agent', models.CharField(blank=True, max_length=512, null=True)),
                ('host', models.CharField(blank=True, max_length=512, null=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('url_redirect', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Logs', to='encurtador.urlredirect')),
            ],
        ),
    ]
