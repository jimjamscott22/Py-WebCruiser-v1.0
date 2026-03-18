from PyQt6.QtCore import QUrl

from py_webcruiser.browser import normalize_url


def test_normalize_url_rejects_blank_values():
    assert normalize_url("") is None
    assert normalize_url("   ") is None


def test_normalize_url_adds_https_to_hostnames():
    assert normalize_url("example.com") == QUrl("https://example.com")


def test_normalize_url_keeps_http_and_https_urls():
    assert normalize_url("http://example.com") == QUrl("http://example.com")
    assert normalize_url("https://example.com/path") == QUrl("https://example.com/path")


def test_normalize_url_rejects_non_web_schemes():
    assert normalize_url("ftp://example.com") is None
