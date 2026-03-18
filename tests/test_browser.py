from PyQt6.QtCore import QUrl

from py_webcruiser.browser import normalize_url


def test_normalize_url_rejects_blank_values():
    assert normalize_url("") is None
    assert normalize_url("   ") is None


def test_normalize_url_adds_http_to_hostnames():
    # QUrl.fromUserInput defaults to http
    assert normalize_url("example.com") == QUrl("http://example.com")


def test_normalize_url_keeps_http_and_https_urls():
    assert normalize_url("http://example.com") == QUrl("http://example.com")
    assert normalize_url("https://example.com/path") == QUrl("https://example.com/path")


def test_normalize_url_rejects_non_web_schemes():
    # FTP is not in the allowed schemes list, so we fallback to a search
    assert normalize_url("ftp://example.com") == QUrl("https://www.google.com/search?q=ftp://example.com")


def test_normalize_url_searches_for_plain_text():
    assert normalize_url("python documentation") == QUrl("https://www.google.com/search?q=python documentation")
