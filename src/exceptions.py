import sys

def error_message_detail(error, error_message_detail: sys):
    _,_,exc_tb = error_message_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "There was an error in your code. Filename: [{0}], on line number: [{1}], with error: [{2}]".format(
        file_name, exc_tb.tb_lineno, error
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_message_detail: sys):
        super().__init__(error_message)