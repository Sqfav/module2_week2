from abc import ABC


class Document:
    def __init__(self, text):
        self.text = text

    def print_document(self, printer):
        printer.print_page(printer, self.text)


class Printer(ABC):
    @staticmethod
    def print_page(self, text):
        print(f'Device: {self.name}')
        print(self.style(text))


class InkjetPrinter(Printer):
    name = 'Inkjet Printer'
    @staticmethod
    def style(text):
        return text.upper()


class LaserPrinter(Printer):
    name = 'Laser Printer'
    @staticmethod
    def style(text):
        return text.lower()

class HPLaserJet(Printer):
    name = 'HPLaserJet Pro 2200'
    @staticmethod
    def style(text):
        return text.swapcase()


if __name__ == "__main__":
    document = Document("Text of the document.")
    try:
        subclasses = Printer.__subclasses__()
        for i, sub in enumerate(subclasses, start=1):
            print(f'{i}: {sub.name}')
        choice = subclasses[int(input('Введи номер выбранного принтера: '))-1]
    except (ValueError, IndexError):
        print('Можно вводить только число, соответствующее номеру принтера. До-сви-да-ни-я.')
    else:
        document.print_document(choice)
