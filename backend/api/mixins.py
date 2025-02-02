import re

CAMEL_REGEX = re.compile(r"(?<=.)_(\w)")
SNAKE_REGEX = re.compile(r"(?<=[a-z])([A-Z])")


def match_upper(match):
    return match.group(1).upper()


def match_snake(match):
    return f"_{match.group(1).lower()}"


def to_camelcase(text):
    return CAMEL_REGEX.sub(match_upper, text)


def to_snake_case(text):
    return SNAKE_REGEX.sub(match_snake, text)


def to_camelcase_data(data):
    """Recursively convert dictionary keys from snake_case to camelCase."""
    if isinstance(data, dict):
        return {to_camelcase(k): to_camelcase_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [to_camelcase_data(datum) for datum in data]
    return data


def to_snake_case_data(data):
    """Recursively convert dictionary keys from camelCase to snake_case."""
    if isinstance(data, dict):
        return {to_snake_case(k): to_snake_case_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [to_snake_case_data(datum) for datum in data]
    return data


class CamelCaseMixin:
    """Mixin to convert API input to snake_case and output to camelCase."""

    def to_representation(self, instance):
        """Convert serialized output to camelCase."""
        data = super().to_representation(instance)
        return to_camelcase_data(data)

    def to_internal_value(self, data):
        """Convert incoming JSON data from camelCase to snake_case."""
        return super().to_internal_value(to_snake_case_data(data))
