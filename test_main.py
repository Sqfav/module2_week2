import unittest
import io
from unittest.mock import patch
from main import Document, InkjetPrinter, LaserPrinter


class TestDocumentPrinting(unittest.TestCase):
    def setUp(self):
        self.inkjet_printer = InkjetPrinter()
        self.laser_printer = LaserPrinter()
        self.text = "string for tests"
        self.document = Document(self.text)

    def test_inkjet_printing(self):
        expected_output = "Device: Inkjet Printer:\n" + self.text + "\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.document.print_document(self.inkjet_printer)
            assert mock_stdout.getvalue() == expected_output

    def test_laser_printing(self):
        expected_output = "Device: Laser Printer:\n" + self.text + "\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.document.print_document(self.laser_printer)
            assert mock_stdout.getvalue() == expected_output


if __name__ == "__main__":
    unittest.main()
