class TestYoutubeVerification:

    def test_training_verified(self):
        text = extract_text()

        assert (
            "fleet expense reporting training"
            in text
        )

        assert "verified" in text