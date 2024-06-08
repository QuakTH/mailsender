from exceptions import CustomException


def run_log_exception(log_output_name: str):
    def run_callable(callable):
        def wrapper(self, *args, **kwargs):
            log_output = getattr(self, log_output_name)
            try:
                callable(self, *args, **kwargs)
            except CustomException as e:
                log_output.append(e.msg)
            except Exception as e:
                print(e)
                log_output.append("Something Went Wrong.. Try to restart the app.")

        return wrapper

    return run_callable
