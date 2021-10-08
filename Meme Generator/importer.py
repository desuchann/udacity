"""Responsible for quote file parsing."""

from abc import ABC, abstractmethod
import docx
import pandas
from string import printable
from engines import QuoteModel

import subprocess
from helpers import CreateTemp


class IncompatiblePathException(TypeError):
    """Throw if the input file isn't compatible with the given class type."""

    pass


class IngestorInterface(ABC):
    """Abstract class from which various interfacce types will inherit."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str):
        """Bool indicating if the inherited class is able to parse the given file input."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path):
        """Abstract class which will be responsible for parsing the quote text files."""
        pass


class DocxImporter(IngestorInterface):
    """Inherited class: word documents."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str):
        """Responsible for parsing quote text files."""
        if not cls.can_ingest(path):
            raise IncompatiblePathException('Cannot ingest this file type')

        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split(' - ')
                quotes.append(QuoteModel(parsed[0].strip('"'), parsed[1]))
        return quotes


class TextImporter(IngestorInterface):
    """Inherited class: text documents."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str):
        """Responsible for parsing quote text files."""
        if not cls.can_ingest(path):
            raise IncompatiblePathException('Cannot ingest this file type')

        quotes = []
        with open(path, "r") as f:
            quotes = []
            for line in f.readlines():
                line = ''.join([x for x in line if x in printable]).strip(
                    '\n\r').strip()
                if len(line) > 0:
                    parsed = line.split(' - ')
                    quotes.append(QuoteModel(parsed[0].strip('"'), parsed[1]))
        return quotes


class CSVImporter(IngestorInterface):
    """Inherited class: csv documents."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str):
        """Responsible for parsing quote text files."""
        if not cls.can_ingest(path):
            raise IncompatiblePathException('Cannot ingest this file type')

        quotes = []
        df = pandas.read_csv(path, header=0)
        for _, row in df.iterrows():
            quotes.append(QuoteModel(row['body'], row['author']))
        return quotes


class PDFImporter(IngestorInterface):
    """Inherited class: pdf documents."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str):
        """Responsible for parsing quote text files."""
        if not cls.can_ingest(path):
            raise IncompatiblePathException('Cannot ingest this file type')

        tmp = CreateTemp()
        filename = tmp.mkfile('txt')
        call = subprocess.run(
            ['pdftotext', str(path).replace('\\', '/'), filename], shell=True)

        with open(filename, "r") as f:
            quotes = []
            for line in f.readlines():  # defaults to .read() as \n aren't correct apparently...
                parts = line.split('"')
                z = zip(parts[1::2], map(
                    lambda x: x.strip(' -\n'), parts[2::2]))
                for pair in z:
                    quotes.append(QuoteModel(pair[0], pair[1]))

        tmp.rmfile()
        return quotes


class Ingestor(IngestorInterface):
    """Main interface for parsing quote files."""

    importers = [CSVImporter, DocxImporter, PDFImporter, TextImporter]

    @classmethod
    def parse(cls, path):
        """Decide which child is capable of digesting the input file and instantiate it accordingly."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
        else:
            raise IncompatiblePathException('Cannae ingest this path type')
