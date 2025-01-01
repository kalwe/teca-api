from quart import request, jsonify
from app.core.utils import TokenUtils  # Utiliza TokenUtils para validar JWT

async def authentication_middleware(request):
    token = request.headers.get("Authorization")

    if not token or not TokenUtils.verify_token(token):
        return jsonify({"message": "Unauthorized"}), 401

    # O token foi verificado com sucesso, então prossiga com a requisição.
    return await request.app.asgi_app(request)
