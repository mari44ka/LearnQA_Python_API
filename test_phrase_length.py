class TestPhraseLength:
    def test_phrase_length(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "the phrase is bigger 15 symbols"
