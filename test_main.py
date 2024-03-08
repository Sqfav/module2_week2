import unittest
import io
from unittest.mock import patch
from main import Document, InkjetPrinter, LaserPrinter, HPLaserJet


class TestDocumentPrinting(unittest.TestCase):
    def setUp(self):
        self.document_text = "yet another test string"
        self.document = Document(self.document_text)

    def test_inkjet_printing(self):
        expected_output = f'Device: Inkjet Printer\n{self.document_text.upper()}\n'
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.document.print_document(InkjetPrinter)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_laser_printing(self):
        expected_output = f'Device: Laser Printer\n{self.document_text.lower()}\n'
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.document.print_document(LaserPrinter)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_hp_laserjet_printing(self):
        expected_output = f'Device: HPLaserJet Pro 2200\n{self.document_text.swapcase()}\n'
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.document.print_document(HPLaserJet)
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
