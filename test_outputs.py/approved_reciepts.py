class TestApprovedReceipts:

    def test_receipt_clear_approved(self):
        text = extract_text()

        assert "bay fuel & grill" in text
        assert "approved" in text

    def test_receipt_blurry_approved(self):
        text = extract_text()

        assert "highway diner" in text
        assert "approved" in text

    def test_receipt_folded_approved(self):
        text = extract_text()

        assert "golden route" in text
        assert "approved" in text