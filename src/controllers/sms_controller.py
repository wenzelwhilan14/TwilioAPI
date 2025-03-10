from flask import Blueprint, request, jsonify
from src.services.twilio_service import send_sms

sms_bp = Blueprint("sms", __name__)

@sms_bp.route("/send", methods=["POST"])
def sms():
    data = request.get_json()
    to = data.get("to")
    message = data.get("message")

    if not to or not message:
        return jsonify({"success": False, "error": "Número y mensaje requeridos"}), 400

    try:
        sid = send_sms(to, message)
        return jsonify({"success": True, "sid": sid})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
