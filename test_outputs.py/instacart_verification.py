class TestInstacartVerification:

    def test_instacart_order_verified(self):
        text = extract_text()

        assert "inst-3982-0426" in text

        assert "verified" in text