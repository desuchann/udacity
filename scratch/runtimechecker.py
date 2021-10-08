import functools
import inspect


def check_types(severity=1):
    if severity == 0:
        return lambda function: function  # all is swell so exit asap

    def _bind_args(function, *args, **kwargs):
        return inspect.signature(function).bind(*args, **kwargs).arguments

    def _alert(ent, exp):
        msg = f'{ent} should be {exp} so this will probably break.'
        if severity == 0:
            return msg
        if severity == 2:
            raise TypeError(msg)

    def checker(function):
        annos = function.__annotations__
        if not annos:
            return function  # as is i.e. skip
        if not all(isinstance(arg, type) for arg in annos.values()):
            _alert(2)  # how have you managed that

        def wrapper(*args, **kwargs):
            for entry in _bind_args(function, *args, **kwargs).items():
                exp = annos[entry[0]]
                if not isinstance(entry[1], exp):
                    _alert(entry[1], exp)
            return function(*args, **kwargs)
        return wrapper
    return checker


@check_types(severity=2)
def foo(a: int, b: str) -> bool:
    return b[a] == 'X'


if __name__ == '__main__':
    foo(1, 1)
