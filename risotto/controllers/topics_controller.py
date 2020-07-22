import math

from flask import Blueprint, jsonify, request

from risotto.models import Topic

bp = Blueprint("topics", __name__, url_prefix="/topics")


@bp.route("/", methods=("GET",))
def get_topics():
    # Query params
    """
    page_param = int(request.args.get("page", "1"))
    items_per_page_param = int(request.args.get("items_per_page", "20"))
    topic_param = request.args.get("topic")
    subtopic_param = request.args.get("subtopic")
    search_param = request.args.get("search")
    """

    # Filtering
    topics, subtopics = Topic.all()

    response = {
        "status": "OK",
        "payload": {"topics": topics, "subtopics": subtopics,},
    }

    return jsonify(response)
