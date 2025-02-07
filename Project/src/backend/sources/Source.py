from unidecode import unidecode

class Source:

    LANGUAGES = ['en', 'pt', 'es', 'fr', 'de', 'it', 'zh']

    @staticmethod
    def sanitize_text(text: str) -> str:
        return unidecode(text)

    @staticmethod
    def group(results: list) -> list:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    def format_output(entity: str, data: list) -> list:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    def search_entity(entity: str, lang: str) -> list:
        raise NotImplementedError("Subclasses must implement this method")
    
    @staticmethod
    def search(entity: str, lang: str) -> list:
        raise NotImplementedError("Subclasses must implement this method")