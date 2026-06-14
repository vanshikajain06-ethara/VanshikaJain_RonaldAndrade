class TestWhatsappEvidence:

    def test_duplicate_submission_flagged(self):
        text = extract_text()

        assert (
            "extra copy attached by mistake"
            in text
        )