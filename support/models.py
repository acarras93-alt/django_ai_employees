from django.contrib.auth.models import User
from django.db import models

from orders.models import Order


class Conversation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="conversations"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="conversations"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Conversation #{self.user} -  {self.user.username} / Order #{self.order}"
        )


class Message(models.Model):
    ROLE_CHOICES = (
        ("user", "User"),
        ("agent", "Agent"),
    )

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="message",
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} - {self.content[:50]}"


class AgentLog(models.Model):
    EVENT_CHOICE = (
        ("support", "Support Agent"),
        ("tool_call", "Toll Call"),
        ("tool_result", "Toll Result"),
        ("manager", "Manager"),
        ("risk", "Risk"),
        ("final", "Final"),
    )

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="agentlogs",
    )
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.event_type}] - {self.message[:40]}"
