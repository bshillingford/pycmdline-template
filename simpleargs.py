import functools, argparse, logging


class arg:
    def __init__(self, *addarg_args, **addarg_kwargs):
        self.addarg_args = addarg_args
        self.addarg_kwargs = addarg_kwargs

    def __call__(self, f):
        if not hasattr(f, "cmdline"):
            raise Exception("Cannot find cmdline attribute of function. "
                            "Did you forget to put cmdline as the innermost decorator?")
        parser = f.cmdline.parser
        parser.add_argument(*self.addarg_args, **self.addarg_kwargs)
        return f


class loglevel:
    def __init__(self, default=logging.INFO, format="%(levelname)s: %(message)s"):
        if default not in [logging.DEBUG, logging.INFO, logging.ERROR]:
            raise Exception("This default log level not implemented.")
        self.default = default
        self.format_str = format

    def __call__(self, f):
        if not hasattr(f, "cmdline"):
            raise Exception("Cannot find cmdline attribute of function. "
                            "Did you forget to put cmdline as the innermost decorator?")
        group = f.cmdline.parser.add_mutually_exclusive_group()
        group.add_argument("-v", "--verbose",
                           dest="log_debug",
                           help="increase verbosity to DEBUG level",
                           action="store_true",
                           default=(self.default == logging.DEBUG))
        group.add_argument("--log-info",
                           dest="log_info",
                           help="set verbosity to INFO level",
                           action="store_true",
                           default=(self.default == logging.INFO))
        group.add_argument("-q", "--quiet",
                           dest="log_error",
                           help="decrease verbosity; only ERRORs or worse",
                           action="store_true",
                           default=(self.default == logging.ERROR))

        def op(log_debug, log_info, log_error, *args, **kwargs):
            if log_debug:
                level = logging.DEBUG
            elif log_info:
                level = logging.INFO
            elif log_error:
                level = logging.ERROR
            else:
                raise Exception("Unexpected case not handled. Fix me.")
            logging.basicConfig(format=self.format_str, level=level)

            return args, kwargs
        f.cmdline.addop(op)

        return f


class cmdline:
    def __init__(self, debug_mode=False, *args, **kwargs):
        self.debug_mode = debug_mode
        self.parser = argparse.ArgumentParser(*args, **kwargs)
        self._ops = []

    def addop(self, op):
        self._ops.append(op)

    def __call__(self, f):
        @functools.wraps(f)
        def wrapped_f(*args, **kwargs):
            if self.debug_mode:
                return f(*args, **kwargs)

            parsed = self.parser.parse_args()
            kwargs.update(vars(parsed))

            for op in self._ops:
                args, kwargs = op(*args, **kwargs)
            return f(*args, **kwargs)
        wrapped_f.cmdline = self
        return wrapped_f

