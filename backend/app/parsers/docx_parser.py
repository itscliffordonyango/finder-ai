from docx import Document


class DOCXParser:

    @staticmethod
    def extract_text(path: str):

        document = Document(path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )