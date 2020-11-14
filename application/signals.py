from flask import got_request_exception
from server import app
from application import models

def log_exception(sender, exception, **extra):
    logException = models.LogException(exception='Got exception during processing: {}'.format(exception))
    logException.save()

got_request_exception.connect(log_exception, app)