class Tweet:
    def __init__(self, id, text, context_annotations={}, entities={}, lang="", possibly_sensitive=False, public_metrics={}, edit_history_tweet_ids={}, withheld={}):
        self.id = id
        self.text = text
        self.context_annotations = context_annotations
        self.entities = entities
        self.lang = lang
        self.possibly_sensitive = possibly_sensitive
        self.public_metrics = public_metrics

    def get(self):
        return {
            "id": self.id,
            "text": self.text,
            "context_annotations": self.context_annotations,
            "entities": self.entities,
            "lang": self.lang, 
            "possibly_sensitive": self.possibly_sensitive,
            "public_metrics": self.public_metrics
        }