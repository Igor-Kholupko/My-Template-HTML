# Generated by Django 2.1.2 on 2018-11-05 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0003_alter_template_file_field_validator_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateHelper',
            fields=[
                ('template',
                 models.OneToOneField(
                     on_delete=django.db.models.deletion.CASCADE,
                     primary_key=True,
                     related_name='helper',
                     serialize=False,
                     to='template.Template')
                 ),
                ('thumbnail',
                 models.CharField(
                     blank=True,
                     null=True,
                     default=None,
                     max_length=260)
                 ),
                ('is_reuploaded',
                 models.BooleanField(
                     default=False)
                 ),
            ],
            options={'verbose_name': 'template meta', 'verbose_name_plural': 'templates meta'},
        ),
    ]