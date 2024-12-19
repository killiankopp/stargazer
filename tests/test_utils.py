from src.utils import extract_field


def test_extract_field():
    data = [{"login": "user1"}, {"login": "user2"}]
    result = extract_field(data, "login")
    assert result == ["user1", "user2"]


def test_extract_field_with_missing_key():
    data = [{"login": "user1"}, {"no_login": "user2"}]
    result = extract_field(data, "login")
    assert result == ["user1"]
