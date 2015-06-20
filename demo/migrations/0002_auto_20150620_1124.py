# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='audience',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_from',
            field=models.DateField(verbose_name='Start date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_to',
            field=models.DateField(help_text='Not required if event is on a single day', blank=True, null=True, verbose_name='End date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_from',
            field=models.TimeField(blank=True, null=True, verbose_name='Start time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_to',
            field=models.TimeField(blank=True, null=True, verbose_name='End time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='first_name',
            field=models.CharField(blank=True, verbose_name='Name', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='last_name',
            field=models.CharField(blank=True, verbose_name='Surname', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], max_length=16),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='embed_url',
            field=models.URLField(blank=True, verbose_name='Embed URL'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
            preserve_default=True,
        ),
    ]
