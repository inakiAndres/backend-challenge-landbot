class Topic:
    VALID_TOPICS = ["sales", "pricing"]

    def __init__(self, topic: str):
        topic = topic.strip().lower()

        if topic not in self.VALID_TOPICS:
            raise ValueError(f"Invalid topic. Allowed values are: {', '.join(self.VALID_TOPICS)}")
        
        self.topic = topic

    def __str__(self):
        return self.topic
