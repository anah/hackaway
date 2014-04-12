# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.language'
        db.add_column(u'article_article', 'language',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=2),
                      keep_default=False)

        # Adding M2M table for field tag on 'Article'
        db.create_table(u'article_article_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_article', models.ForeignKey(orm[u'article.article'], null=False)),
            ('to_article', models.ForeignKey(orm[u'article.article'], null=False))
        ))
        db.create_unique(u'article_article_tag', ['from_article_id', 'to_article_id'])


        # Changing field 'Article.category'
        db.alter_column(u'article_article', 'category', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Article.title'
        db.alter_column(u'article_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):
        # Deleting field 'Article.language'
        db.delete_column(u'article_article', 'language')

        # Removing M2M table for field tag on 'Article'
        db.delete_table('article_article_tag')


        # Changing field 'Article.category'
        db.alter_column(u'article_article', 'category', self.gf('django.db.models.fields.CharField')(max_length=225))

        # Changing field 'Article.title'
        db.alter_column(u'article_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=225))

    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tag_rel_+'", 'to': u"orm['article.Article']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['article']