class Document:
    def __init__(self, text):
        self.text = text

    def print_document(self, printer):
        printer.print_page(self.text)


class InkjetPrinter:
    @staticmethod
    def print_page(text):
        print("Device: Inkjet Printer:")
        print(text)


class LaserPrinter:
    @staticmethod
    def print_page(text):
        print("Device: Laser Printer:")
        print(text)


if __name__ == "__main__":
    document = Document("Text of the document.")

    inkjet_printer = InkjetPrinter()
    laser_printer = LaserPrinter()

    document.print_document(inkjet_printer)
    print("-----------")
    document.print_document(laser_printer)
