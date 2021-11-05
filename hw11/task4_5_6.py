from itertools import groupby
from typing import Type, List
from enum import Enum
from uuid import uuid4
from abc import ABC


class Location(Enum):
    IN_STOCK = 'stock'
    BOOKKEEPING = 'bookkeeping'
    RnD = 'research'
    SECRETARY = 'secretary'


class Vendor(Enum):
    HP = 'Hewlett Packard'
    XEROX = 'Xerox'
    CANON = 'Canon'
    BROTHER = 'Brother'


class PrinterType(Enum):
    MATRIX = 'Matrix printer'
    INKJET = 'Inkjet printer'
    LASER = 'Laser printer'
    THERMAL = 'Thermal printer'
    LED = 'LED printer'


class ScannerType(Enum):
    FLATBED = 'Flatbed scanner'
    DUPLEX = 'Duplex flatbed scanner'
    HANDLED = 'Portable handled scanner'


class OfficeEquipment(ABC):
    def __init__(self, vendor: Vendor, model: str, serial: str, location: Location = Location.IN_STOCK):
        self.vendor = vendor
        self.model = model
        self.serial = serial
        self.location = location
        self.uid = uuid4().int

    def __hash__(self):  # элементы могут быть ключами словаря. От идеи пришлось отказаться, а код остался.
        return self.uid

    def __str__(self):
        return f'{self.vendor.value} {self.model} (S/N: {self.serial})'


class Printer(OfficeEquipment):
    def __init__(self, vendor, model, serial, print_dpi: int, printer_type: PrinterType, is_duplex: bool):
        super().__init__(vendor=vendor, model=model, serial=serial)
        self.print_dpi = print_dpi
        self.printer_type = printer_type
        self.is_duplex = is_duplex

    def __hash__(self):
        return super().__hash__()

    def __str__(self):
        common_props = OfficeEquipment.__str__(self)
        duplex = ' (duplex)' if self.is_duplex else ''
        return f'{common_props}, {self.printer_type.value}{duplex}, {self.print_dpi} DPI'


class Scanner(OfficeEquipment):
    def __init__(self, vendor, model, serial, scan_dpi: int, scanner_type: ScannerType):
        super().__init__(vendor=vendor, model=model, serial=serial)
        self.scan_dpi = scan_dpi
        self.scanner_type = scanner_type

    def __hash__(self):
        return super().__hash__()

    def __str__(self):
        common_props = OfficeEquipment.__str__(self)
        return f'{common_props}, {self.scanner_type.value}, {self.scan_dpi} DPI'


# Интереснее было бы сделать через множественное наследование - MFP(Printer, Scanner),
# так как они друг друга дополняют, но соорудить для этого валидный конструктор мне не удалось.
class MFP(Printer):
    def __init__(self, vendor, model, serial, print_dpi: int, printer_type: PrinterType, is_duplex: bool,
                 scan_dpi: int, scanner_type: ScannerType):
        super().__init__(vendor, model, serial, print_dpi, printer_type, is_duplex)
        self.scan_dpi = scan_dpi
        self.scanner_type = scanner_type

    def __hash__(self):
        return super().__hash__()

    def __str__(self):
        common = OfficeEquipment.__str__(self)
        printer_props = Printer.__str__(self).replace(common, '')
        return f'{common}{printer_props}, {self.scanner_type.value}, {self.scan_dpi} DPI'


class Warehouse:
    def __init__(self, *args):
        self.__in_stock = []
        self.__in_use = []
        self.__in_stock_count = 0
        self.__in_use_count = 0
        self.to_stock(*args)

    def __str__(self):
        return f'Warehouse: {self.in_stock_count} in stock, {self.in_use_count} in use.'

    @property
    def in_stock_count(self):
        return self.__in_stock_count

    @property
    def in_use_count(self):
        return self.__in_use_count

    @in_stock_count.setter
    def in_stock_count(self, value):
        pass  # сеттер недоступен извне

    @in_use_count.setter
    def in_use_count(self, value):
        pass  # сеттер недоступен извне

    @property
    def stock(self) -> List[OfficeEquipment]:
        return self.__in_stock

    @property
    def in_use(self) -> List[OfficeEquipment]:
        return self.__in_use

    @stock.setter
    def stock(self, value):
        pass  # сеттер недоступен извне

    @in_use.setter
    def in_use(self, value):
        pass  # сеттер недоступен извне

    @staticmethod
    def __validate_arg(arg, type_: Type[OfficeEquipment] = OfficeEquipment):
        if not isinstance(arg, type_):
            raise ValueError('Arguments must be OfficeEquipment instances.')

    def __update_status(self):
        self.__in_stock_count = len(self.__in_stock)
        self.__in_use_count = len(self.__in_use)

    def to_stock(self, *args: Type[OfficeEquipment]):
        for device in args:
            try:
                self.__validate_arg(device)
            except ValueError:
                print(f' > ERROR: {device} is not OfficeEquipment')
                continue
            device.location = Location.IN_STOCK
            if device in self.__in_use:
                self.__in_use.remove(device)
            self.__in_stock.append(device)
        self.__update_status()

    def to_unit(self, *args: Type[OfficeEquipment], unit: Location):
        for device in args:
            try:
                self.__validate_arg(device)
            except ValueError:
                print(f' > ERROR: {device} is not OfficeEquipment')
                continue
            if device not in self.__in_stock:  # передача между подразделениями - только через склад
                self.to_stock(device)
            device.location = unit
            self.__in_stock.remove(device)
            self.__in_use.append(device)
        self.__update_status()

    def stats(self):
        return {group.value: len(list(items)) for group, items in
                groupby(self.__in_stock + self.__in_use, lambda x: x.location)}


supply_1 = [
    MFP(
        vendor=Vendor.XEROX,
        model='WorkCentre 3335',
        serial='HD73HFOE2HF',
        print_dpi=1200,
        printer_type=PrinterType.LASER,
        is_duplex=True,
        scan_dpi=2400,
        scanner_type=ScannerType.DUPLEX,
    ),
    MFP(
        vendor=Vendor.BROTHER,
        model='MFC-L2700DWR',
        serial='HD73HFOE2HF',
        print_dpi=1200,
        printer_type=PrinterType.LASER,
        is_duplex=True,
        scan_dpi=2400,
        scanner_type=ScannerType.DUPLEX,
    ),
    'some printer',
    Printer(
        vendor=Vendor.HP,
        model='LaserJet M404dn',
        serial='XYZ12345',
        print_dpi=1200,
        printer_type=PrinterType.LASER,
        is_duplex=True,
    ),
    Printer(
        vendor=Vendor.HP,
        model='OfficeJet 202',
        serial='JSYE6HRIF39',
        print_dpi=1200,
        printer_type=PrinterType.INKJET,
        is_duplex=False,
    ),
    Printer(
        vendor=Vendor.XEROX,
        model='С230',
        serial='3HD93IRHF01',
        print_dpi=600,
        printer_type=PrinterType.LED,
        is_duplex=False,
    ),
    Scanner(
        vendor=Vendor.HP,
        model='ScanJet Pro 3500',
        serial='84S63G58F3K9S',
        scan_dpi=1200,
        scanner_type=ScannerType.DUPLEX,
    ),
    Scanner(
        vendor=Vendor.CANON,
        model='Canoscan LIDE300',
        serial='10119292019',
        scan_dpi=2400,
        scanner_type=ScannerType.DUPLEX,
    ),
    Scanner(
        vendor=Vendor.CANON,
        model='imageFORMULA P-208II',
        serial='8481038475101',
        scan_dpi=600,
        scanner_type=ScannerType.HANDLED,
    ),
    MFP(
        vendor=Vendor.XEROX,
        model='WorkCentre 3335',
        serial='HD73HFOE2HF',
        print_dpi=1200,
        printer_type=PrinterType.LASER,
        is_duplex=True,
        scan_dpi=2400,
        scanner_type=ScannerType.DUPLEX,
    ),
    MFP(
        vendor=Vendor.BROTHER,
        model='MFC-L2700DWR',
        serial='HD73HFOE2HF',
        print_dpi=1200,
        printer_type=PrinterType.LASER,
        is_duplex=True,
        scan_dpi=2400,
        scanner_type=ScannerType.DUPLEX,
    ),
    Printer(
        vendor=Vendor.HP,
        model='LaserJet M404dn',
        serial='XYZ12345',
        print_dpi=1200,
        printer_type=PrinterType.LASER,
        is_duplex=True,
    ),
    Printer(
        vendor=Vendor.HP,
        model='OfficeJet 202',
        serial='JSYE6HRIF39',
        print_dpi=1200,
        printer_type=PrinterType.INKJET,
        is_duplex=False,
    ),
]

supply_2 = [
    Printer(
        vendor=Vendor.XEROX,
        model='С230',
        serial='3HD93IRHF01',
        print_dpi=600,
        printer_type=PrinterType.LED,
        is_duplex=False,
    ),
    Scanner(
        vendor=Vendor.HP,
        model='ScanJet Pro 3500',
        serial='84S63G58F3K9S',
        scan_dpi=1200,
        scanner_type=ScannerType.DUPLEX,
    ),
    Scanner(
        vendor=Vendor.CANON,
        model='Canoscan LIDE300',
        serial='10119292019',
        scan_dpi=2400,
        scanner_type=ScannerType.DUPLEX,
    ),
    'some Honeywell scanner',
    Scanner(
        vendor=Vendor.CANON,
        model='imageFORMULA P-208II',
        serial='8481038475101',
        scan_dpi=600,
        scanner_type=ScannerType.HANDLED,
    ),
]

if __name__ == '__main__':
    print('Инициируем объект склада всместе с первой поставкой техники')
    warehouse = Warehouse(*supply_1)
    print(warehouse)

    print('\nДобавляем технику из второй поставки')
    warehouse.to_stock(*supply_2)
    print(warehouse)

    print('\nВыдаем рандомную технику в отделы')
    devices_for_bookkeeping = warehouse.stock[:4]
    warehouse.to_unit(*devices_for_bookkeeping, unit=Location.BOOKKEEPING)
    print(warehouse)
    devices_for_secretary = warehouse.stock[10:13]
    warehouse.to_unit(*devices_for_secretary, unit=Location.SECRETARY)
    print(warehouse)
    devices_for_RnD = warehouse.stock[:-2]
    warehouse.to_unit(*devices_for_RnD, unit=Location.RnD)
    print(warehouse)

    print('\nСмотрим складские учеты')
    print(warehouse.stats())
    for item in warehouse.in_use:
        print(f'{item.location.value.capitalize()}\t-\t{item}')

    print('\nВозвращаем все на склад')
    warehouse.to_stock(*warehouse.in_use)
    print(warehouse)
