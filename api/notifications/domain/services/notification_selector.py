class NotificationSelector:

    @staticmethod
    def get_notification_channel(topic: str) -> str:
        """Returns the channel to use based on the topic."""
        if topic == "sales":
            return "slack"
        elif topic == "pricing":
            return "email"
