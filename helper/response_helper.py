class ResponseModel:
    def __init__(self, message, response_type, data=None, errors=None):
        self.message = message
        self.type = response_type
        self.data = data
        self.errors = errors

    def to_json(self):
        response = {"message": self.message, "type": self.type}
        if self.data:
            response["data"] = self.data
        if self.errors:
            response["errors"] = self.errors
        return response


class SuccessResponse(ResponseModel):
    def __init__(self, message, data=None):
        super().__init__(message, "success", data=data)


class ErrorResponse(ResponseModel):
    def __init__(self, message, errors=None):
        super().__init__(message, "failed", errors=errors)
