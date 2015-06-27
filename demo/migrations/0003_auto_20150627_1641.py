# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20150620_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='choices',
            field=models.CharField(blank=True, verbose_name='Choices', help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='default_value',
            field=models.CharField(blank=True, verbose_name='Default value', help_text='Default value. Comma separated values supported for checkboxes.', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(verbose_name='Field type', choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], max_length=16),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='help_text',
            field=models.CharField(blank=True, verbose_name='Help text', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='label',
            field=models.CharField(verbose_name='Label', help_text='The label of the form field', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='required',
            field=models.BooleanField(default=True, verbose_name='Required'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formpage',
            name='from_address',
            field=models.CharField(blank=True, verbose_name='From address', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formpage',
            name='subject',
            field=models.CharField(blank=True, verbose_name='Subject', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formpage',
            name='to_address',
            field=models.CharField(blank=True, verbose_name='To address', help_text='Optional - form submissions will be emailed to this address', max_length=255),
            preserve_default=True,
        ),
    ]
