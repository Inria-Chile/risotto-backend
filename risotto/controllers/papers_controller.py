import math

from flask import Blueprint, jsonify, request

from risotto.models import Paper

bp = Blueprint("papers", __name__, url_prefix="/papers")


@bp.route("/", methods=("GET",))
def get_papers():
    # Query params
    page_param = int(request.args.get("page", "1"))
    items_per_page_param = int(request.args.get("items_per_page", "20"))
    topic_param = request.args.get("topic", "")
    subtopic_param = request.args.get("subtopic", "")
    search_param = request.args.get("search", "")

    if len(topic_param) == 0 and len(subtopic_param) > 0:
        response = {
            "status": "error",
            "msg": "Can't specify subtopic parameter if a topic parameter is not provided",
        }
        return jsonify(response), 400

    if len(subtopic_param) > 0 and subtopic_param.split("-")[0] != topic_param:
        response = {
            "status": "error",
            "msg": "Subtopic parameter doesn't belong to the specified topic parameter",
        }
        return jsonify(response), 400

    # Filtering
    papers_df = Paper.all()
    filtered_df = Paper.filter(
        papers_df, topic=topic_param, subtopic=subtopic_param, search=search_param
    )
    sorted_df = Paper.sort(filtered_df, by="pagerank", ascending=False)

    # Perform pagination
    num_papers = len(sorted_df)
    num_pages = math.ceil(num_papers / items_per_page_param)
    start_idx, end_idx = (
        (page_param - 1) * items_per_page_param,
        page_param * items_per_page_param,
    )
    papers_page = sorted_df.iloc[start_idx:end_idx]
    papers_serialized = [
        {"rank": idx + 1, **paper}
        for paper, idx in zip(
            papers_page.to_dict(orient="records"), range(start_idx, end_idx)
        )
    ]

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
