import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic

# define MATRIX_ROWS 6
# define MATRIX_COLS 9
# define MATRIX_COL_PINS { D1,D0,D4,C6,D7,E6,B4,F4,F5 }
# define MATRIX_ROW_PINS { F6,F7,B1,B3,B2,B6 }

# define DIODE_DIRECTION COL2ROW
# define USE_SERIAL
# define SPLIT_USB_DETECT
# define MASTER_LEFT
# define SOFT_SERIAL_PIN D3

# define BACKLIGHT_PIN B5

# ['__class__', '__name__',
# 'A0', 'A1', 'A2', 'A3', 'GP0', 'GP1', 'GP10', 'GP11', 'GP12', 'GP13', 'GP14',
# 'GP15', 'GP16', 'GP17', 'GP18', 'GP19', 'GP2', 'GP20', 'GP21', 'GP22', 'GP23',
# 'GP24', 'GP25', 'GP26', 'GP26_A0', 'GP27', 'GP27_A1', 'GP28', 'GP28_A2', 'GP3',
#  'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'LED', 'SMPS_MODE', 'VBUS_SENSE', 'VOLTAGE_MONITOR', 'board_id']


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP4, # black
        board.GP5, # red
        board.GP6, # white
        board.GP7, # yellow
        board.GP8, # orange
        board.GP9, # green
        board.GP10, # blue
        board.GP11, # purple
        board.GP12, # red2
    )
    row_pins = (
        board.GP28, # purple
        board.GP27, # blue
        board.GP26, # green
        board.GP22, # orange
        board.GP21, # yellow
        board.GP20, # white
    )
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = board.GP0
    data_pin2 = board.GP1
    led_pin = board.GP13 # red3
    coord_mapping = []
    coord_mapping.extend(ic(0, x) for x in range(18))
    coord_mapping.extend(ic(1, x) for x in range(18))
    coord_mapping.extend(ic(2, x) for x in range(18))
    coord_mapping.extend(ic(3, x) for x in range(18))
    coord_mapping.extend(ic(4, x) for x in range(18))
    coord_mapping.extend(ic(5, x) for x in range(18))
