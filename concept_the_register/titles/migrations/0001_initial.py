# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Title'
        db.create_table(u'titles_title', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'titles', ['Title'])


    def backwards(self, orm):
        # Deleting model 'Title'
        db.delete_table(u'titles_title')


    models = {
        u'titles.title': {
            'Meta': {'object_name': 'Title'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['titles']