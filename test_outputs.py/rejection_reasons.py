class TestRejectionReasons:

    def test_duplicate_reason_present(self):
        text = extract_text()

        assert "duplicate receipt" in text

    def test_missing_receipt_reason_present(self):
        text = extract_text()

        assert "missing receipt" in text