from strictdoc.helpers.string import (
    interpolate_at_pattern_lazy,
    is_safe_alphanumeric_string,
    sanitize_html_form_field,
)


def test_sanitize_01_trims_all_fields_in_initializer_spaces():
    field = """
        Hello world!        
    """  # noqa: W291
    sanitized_field = sanitize_html_form_field(field, multiline=False)
    assert sanitized_field == "Hello world!"

    sanitized_field = sanitize_html_form_field(field, multiline=True)
    assert sanitized_field == "Hello world!"


def test_sanitize_02_trims_all_fields_in_initializer_newlines():
    field = """
        \n\n    Hello world!   \n\n     
    """  # noqa: W291
    sanitized_field = sanitize_html_form_field(field, multiline=False)
    assert sanitized_field == "Hello world!"

    sanitized_field = sanitize_html_form_field(field, multiline=True)
    assert sanitized_field == "Hello world!"


def test_sanitize_10_removes_all_trailing_whitespace_in_initializer():
    # section statement below contains newlines:
    field = """
Hello world!    

Hello world!    

Hello world!    
    """  # noqa: W291
    sanitized_field = sanitize_html_form_field(field, multiline=True)
    assert sanitized_field == "Hello world!\n\nHello world!\n\nHello world!"


def test_sanitize_04_single_line_removes_all_newlines():
    field = """
        Hello world!        
        Hello world!
        Hello world!
    """  # noqa: W291
    sanitized_field = sanitize_html_form_field(field, multiline=False)
    assert sanitized_field == "Hello world! Hello world! Hello world!"


def test_is_safe_alphanumeric_string():
    assert is_safe_alphanumeric_string("") is False
    assert is_safe_alphanumeric_string("/") is False
    assert is_safe_alphanumeric_string("/document.sdoc") is False
    assert is_safe_alphanumeric_string("doc#%ument.sdoc") is False

    assert is_safe_alphanumeric_string("document") is True
    assert is_safe_alphanumeric_string("document.sdoc") is True
    assert is_safe_alphanumeric_string("document.ext.sdoc") is True
    assert is_safe_alphanumeric_string("docs/document.ext.sdoc") is True
    assert is_safe_alphanumeric_string("docs/docs2/document.sdoc") is True
    assert is_safe_alphanumeric_string("docs/document1.sdoc") is True


def test_interpolate_at_pattern_lazy():
    def resolver(variable_name):
        replacements = {"GIT_VERSION": "abcd123", "GIT_BRANCH": "main"}
        return replacements[variable_name]

    result = interpolate_at_pattern_lazy("@GIT_VERSION, @GIT_BRANCH", resolver)
    assert result == "abcd123, main"

    result = interpolate_at_pattern_lazy("foo, bar", resolver)
    assert result == "foo, bar"
