from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def get_info():
    uid = request.args.get("id")
    if not uid:
        return jsonify({
            "developer": "BIMO BOT",
            "error": "missing id"
        }), 400

    try:
        # جلب البيانات من API الأصلي
        url = f"https://x7ama-info.vercel.app/xInFo?u={uid}"
        res = requests.get(url, timeout=10)
        res.raise_for_status()

        data = res.json()  # البيانات كما هي من API الأصلي

        # تعديل الرد لإضافة اسم المطور
        response = {
            "developer": "BIMO BOT",
            "user_id": uid,
            "data": data
        }

        return jsonify(response)

    except requests.exceptions.RequestException as e:
        return jsonify({
            "developer": "BIMO BOT",
            "error": "حدث خطأ أثناء جلب البيانات",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)