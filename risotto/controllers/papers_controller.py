import math

from flask import Blueprint, jsonify, request

from risotto.models import Paper

bp = Blueprint("papers", __name__, url_prefix="/papers")


@bp.route("/", methods=("GET",))
def get_papers():
    # Query params
    page_param = int(request.args.get("page", "1"))
    items_per_page_param = int(request.args.get("items_per_page", "20"))
    topic_param = request.args.get("topic")
    subtopic_param = request.args.get("subtopic")
    search_param = request.args.get("search")

    if topic_param is None and subtopic_param is not None:
        response = {
            "status": "error",
            "msg": "Can't specify subtopic parameter if a topic parameter is not provided",
        }
        return jsonify(response), 400

    # Filtering
    papers_df = Paper.all()
    filtered_df = Paper.filter(
        papers_df, topic=topic_param, subtopic=subtopic_param, search=search_param
    )

    # Perform pagination
    num_papers = len(filtered_df)
    num_pages = math.ceil(num_papers / items_per_page_param)
    start_idx, end_idx = (
        (page_param - 1) * items_per_page_param,
        page_param * items_per_page_param,
    )
    papers_page = filtered_df.iloc[start_idx:end_idx]
    papers_serialized = papers_page.to_dict(orient="records")

    response = {
        "status": "OK",
        "payload": {
            "papers": papers_serialized,
            "num_results": num_papers,
            "num_pages": num_pages,
            "page": page_param,
        },
    }

    return jsonify(response)
