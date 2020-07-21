import math

from flask import Blueprint, jsonify, request

from risotto.models import Paper

bp = Blueprint("papers", __name__, url_prefix="/papers")


@bp.route("/", methods=("GET",))
def get_papers():
    # Query params
    page = int(request.args.get("page", "1"))
    items_per_page = int(request.args.get("items_per_page", "20"))
    papers_df = Paper.all()
    masked_df = papers_df
    num_papers = len(masked_df)
    num_pages = math.ceil(num_papers / items_per_page)
    start_idx, end_idx = (page - 1) * items_per_page, page * items_per_page
    papers_page = masked_df.iloc[start_idx:end_idx]
    papers_serialized = papers_page.to_dict(orient="records")
    response = {
        "status": "OK",
        "payload": papers_serialized,
        "num_pages": num_pages,
        "page": page,
    }
    return jsonify(response)
