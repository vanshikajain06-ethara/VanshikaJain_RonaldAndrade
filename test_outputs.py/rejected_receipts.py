class TestRejectedReceipts:

    def test_duplicate_receipt_rejected(self):
        text = extract_text()

        assert "duplicate" in text

    def test_roadstop_rejected(self):
        text = extract_text()

        assert "roadstop market" in text
        assert "rejected" in text