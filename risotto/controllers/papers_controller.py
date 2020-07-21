from flask import Blueprint, jsonify

from risotto.models import Paper

bp = Blueprint("papers", __name__, url_prefix="/papers")


@bp.route("/", methods=("GET",))
def get_papers():
    papers = Paper.all()
    response = {"status": "OK", "payload": papers.iloc[:10].to_dict(orient="records")}
    return jsonify(response)
