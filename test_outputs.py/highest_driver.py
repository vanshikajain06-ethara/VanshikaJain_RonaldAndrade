class TestDriverAnalysis:

    def test_highest_driver(self):
        text = extract_text()

        assert "michael torres" in text

        assert (
            "highest verified reimbursement"
            in text
        )