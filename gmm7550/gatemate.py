
from enum import Enum

class CFG_mode(Enum):
    SPI_ACTIVE_0 = 0b0000
    SPI_ACTIVE_1 = 0b0001
    SPI_ACTIVE_2 = 0b0010
    SPI_ACTIVE_3 = 0b0011
    SPI_PASSIVE_0 = 0b0100
    SPI_PASSIVE_1 = 0b0101
    SPI_PASSIVE_2 = 0b0110
    SPI_PASSIVE_3 = 0b0111
    JTAG = 0b1100
