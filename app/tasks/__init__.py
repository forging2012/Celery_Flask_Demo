from flask import Blueprint
celery_tasks = Blueprint('celery_tasks', __name__)
from . import tasks