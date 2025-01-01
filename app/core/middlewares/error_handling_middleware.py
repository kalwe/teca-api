from quart import jsonify

async def error_handling_middleware(request):
    try:
        # Tente processar a requisição
        response = await request.app.asgi_app(request)
    except Exception as e:
        # Se ocorrer algum erro, capture e retorne uma resposta personalizada
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    return response
