class ValueObjectError(ValueError):
    pass


class ValueObjectEnumError(ValueObjectError):
    pass


class UUIDValueError(ValueObjectError):
    def __init__(self, value) -> None:
        super().__init__(f"Value={value} is not a correct UUID")


class EmailAddressError(ValueObjectError):
    def __init__(self, value) -> None:
        super().__init__(f"Value={value} is not a correct Email Address")
