class TestTotals:

    def test_total_approved_amount(self):
        text = extract_text()

        assert "$148.35" in text

    def test_total_rejected_amount(self):
        text = extract_text()

        assert "$112.90" in text