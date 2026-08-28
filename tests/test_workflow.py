from workflow import run_mitra


def test_empty_input():
    result = run_mitra("")

    assert result["success"] is False
    assert result["answer"] == "Please enter a question."


def test_whitespace_input():
    result = run_mitra("   ")

    assert result["success"] is False
    assert result["answer"] == "Please enter a question."