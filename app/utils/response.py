from http import HTTPStatus

def success_response(data, status_code=HTTPStatus.OK):
    return {"status": "success", "data": data}, status_code

def error_response(message, status_code=HTTPStatus.NOT_FOUND):
    return {"status": "error", "message": message}, status_code
