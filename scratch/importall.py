from importer import CSVImporter, DocxImporter, IncompatiblePathException, ImportInterface, PDFImporter
from pathlib import Path

class Importer(ImportInterface):
    importers = [CSVImporter, DocxImporter, PDFImporter]

    @classmethod
    def parse(cls, path):
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
        else:
            raise IncompatiblePathException('Cannae disgest this path type')


if __name__ == '__main__':
    # print(Importer.parse(Path('./udacity/web') / 'cats.docx'))
    # print(Importer.parse(Path('./udacity/web') / 'cats.csv'))
    print(Importer.parse(Path('./udacity/web') / 'cats.pdf'))
