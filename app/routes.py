from flask import Blueprint

from app.utils import get_welcome_message, get_health_status

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return get_welcome_message()


@main.route("/health")
def health():
    return get_health_status()
