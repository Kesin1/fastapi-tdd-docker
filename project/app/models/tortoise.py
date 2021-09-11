from tortoise import fields, models


class TextSummary(models.Model):
    """
    New Database model called TextSummary
    """

    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField()

    def __str__(self):
        return self.url
