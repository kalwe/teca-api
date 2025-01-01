import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

async def logging_middleware(request):
    method = request.method
    url = request.url
    timestamp = datetime.utcnow()

    logging.info(f"{timestamp} - {method} {url}")

    # Continuar com a execução da requisição
    return await request.app.asgi_app(request)
