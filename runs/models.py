from django.db import models

from mongoengine import Document, EmbeddedDocument, fields

class Run(Document):
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    user = fields.ListField(fields.EmbeddedDocumentField(User))
    inputs = fields.ListField(fields.EmbeddedDocumentField(ToolInput))

class ToolInput(EmbeddedDocument):
    name = fields.StringField(required=True)
    value = fields.DynamicField(required=True)
