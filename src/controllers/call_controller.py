from flask import Blueprint, request, jsonify
from src.services.twilio_service import make_call

call_bp = Blueprint("calls", __name__)

@call_bp.route("/make", methods=["POST"])
def call():
    data = request.get_json()
    to = data.get("to")
    message = data.get("message")

    if not to or not message:
        return jsonify({"success": False, "error": "Número y mensaje requeridos"}), 400

    try:
        sid = make_call(to, message)
        return jsonify({"success": True, "sid": sid})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
