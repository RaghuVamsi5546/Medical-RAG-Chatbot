import sys

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        self.original_error = error_detail
        _, _, exc_tb = sys.exc_info()
        self.error_message = self._get_detailed_error_message(message, exc_tb)
        super().__init__(self.error_message)

    def _get_detailed_error_message(self, message: str, exc_tb):
        error_info = f" | Error: {self.original_error}" if self.original_error else ""
        if exc_tb is None:
            return f"{message}{error_info}"
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"{message}{error_info} | File: {file_name} | Line: {line_number}"

    def __str__(self):
        return self.error_message
