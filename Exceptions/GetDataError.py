class GetDataError(Exception):
    def __init__(self, extra_info):
        message = f"Неправильные входные данные в поле {extra_info}"
        super().__init__(message)


