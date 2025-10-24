from actionspro.parser import text_parser


def test_text_parser():
    sample_text = "This is a sample text for parsing."
    result = text_parser(sample_text)
    assert result == "This is a sample text for parsing. - parsed"
