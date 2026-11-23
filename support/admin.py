from django.contrib import admin

from .models import AgentLog, Conversation, Message


class ConversationAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


class AgentLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(AgentLog, AgentLogAdmin)
