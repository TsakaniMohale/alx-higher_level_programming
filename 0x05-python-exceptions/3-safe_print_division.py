#!/usr/bin/python3
def safe_print_division9(a, b):
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
