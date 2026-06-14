class TestReportSections:

    def test_summary_section(self):
        text = extract_text()

        assert "summary" in text

    def test_discrepancy_section(self):
        text = extract_text()

        assert "discrepancy" in text

    def test_reimbursement_section(self):
        text = extract_text()

        assert "reimbursement" in text