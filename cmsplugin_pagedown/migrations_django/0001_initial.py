# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagedownConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('markdown', models.TextField()),
                ('html', models.TextField()),
                ('plaintext', models.TextField()),
                ('css_id', models.CharField(help_text=b'Add an optional CSS ID to the rendered outputs wrapping element', max_length=50, blank=True)),
                ('css_classes', models.CharField(help_text=b'Add CSS classes to the rendered outputs wrapper element', max_length=50, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
