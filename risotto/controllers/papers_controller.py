from flask import Blueprint, jsonify

from risotto.models import Paper

bp = Blueprint("papers", __name__, url_prefix="/papers")


@bp.route("/", methods=("GET",))
def get_papers():
    papers = Paper.query.all()
    return jsonify(papers)
