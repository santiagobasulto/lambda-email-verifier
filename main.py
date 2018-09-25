import logging
from flask import Flask, request, make_response, jsonify

import utils
from invalid_domains import INVALID_DOMAIN_SETS


app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


@app.route('/', methods=['POST'])
def lambda_handler(event=None, context=None):
    if not request.is_json:
        return make_response(jsonify(error="Only JSON Supported"), 400)

    data = request.get_json()
    email = data.get('email')
    validate_email = data.get('validate_email', False)
    extra_invalid_domains = data.get('extra_invalid_domains', [])

    if not email:
        return make_response(
            jsonify(error="'email' parameter is required"), 400)

    if validate_email and not utils.is_valid_email(email):
        return jsonify(valid=False, fails={'domain': None, 'email': False})

    domain = utils.extract_domain(email)

    if not domain:
        return make_response(jsonify(error="Can't get domain from email"), 400)

    if domain in INVALID_DOMAIN_SETS:
        return jsonify(valid=False, fails={'domain': True, 'email': None})

    if extra_invalid_domains and domain in extra_invalid_domains:
        return jsonify(valid=False, fails={'domain': True, 'email': None})

    return jsonify(valid=True)


if __name__ == '__main__':
    app.run(debug=False)
