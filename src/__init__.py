from .logger import *
import sys

class customException(Exception):
    
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self._get_detailed_error_message(error_message, error_detail)

    def _get_detailed_error_message(self, error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return f"Error occurred in script: {file_name} at line {line_number}: {error_message}"
        else:
            return f"Error: {error_message}"