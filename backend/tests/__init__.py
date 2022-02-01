from app.main import build_api


def test_main():
    assert build_api() is not None
