class TestArtifactExists:

    def test_output_pdf_exists(self):
        assert os.path.exists(
            OUTPUT_FILE
        ), "Final audit report PDF not found"