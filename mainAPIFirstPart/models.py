from django.db import models


class IdentifierCode(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "{0}-{1}".format(self.identifier, self.code)


class LogMessage(models.Model):
    id_identifier_code = models.ForeignKey(IdentifierCode, on_delete=models.SET_NULL, null=True)
    text_message = models.TextField()

    def __str__(self):
        return "{0}: '{1}'".format(self.id_identifier_code, self.text_message)
