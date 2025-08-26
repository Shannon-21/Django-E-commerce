from django.contrib import admin

from .conversation_models import Conversation, ConversationMessage

admin.site.register(Conversation)
admin.site.register(ConversationMessage)
