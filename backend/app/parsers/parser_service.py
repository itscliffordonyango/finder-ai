from pathlib import Path

from app.parsers.docx_parser import DOCXParser
from app.parsers.pdf_parser import PDFParser


class ParserService:

    @staticmethod
    def parse(path: str):

        extension = Path(path).suffix.lower()

        if extension == ".pdf":
            return PDFParser.extract_text(path)

        if extension == ".docx":
            return DOCXParser.extract_text(path)

        raise ValueError(
            "Unsupported resume format."
        )