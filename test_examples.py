class TestExamples:
    def test_vvod(self):
        phrase = input("Введите фразу: ")
        assert len(phrase) < 15, f"Фраза слишком длинная: {len(phrase)}. Символов максимум 14"
