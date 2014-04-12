# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'tag_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en', max_length=2)),
        ))
        db.send_create_signal(u'tag', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'tag_tag')


    models = {
        u'tag.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'tag_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['tag']