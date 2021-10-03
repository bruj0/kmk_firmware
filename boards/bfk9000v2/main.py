from kb import KMKKeyboard
from kmk.extensions.led import LED
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()
keyboard.debug_enabled = True
# Adding extensions
led_ext = LED(led_pin=keyboard.led_pin)

# TODO Comment one of these on each side
split_side = SplitSide.LEFT
split = Split(
    split_type=SplitType.UART,
    split_side=split_side,
    data_pin=keyboard.data_pin,
    data_pin2=keyboard.data_pin2,
)

layers_ext = Layers()

keyboard.modules = [layers_ext, split]
keyboard.extensions = [led_ext]
#
# Cleaner key names
_______ = KC.TRNS
XXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)

LED_TOG = KC.LED_TOG  # Toggles LED's
LED_INC = KC.LED_INC  # Increase Brightness
LED_DEC = KC.LED_DEC  # Decrease Brightness
LED_ANI = KC.LED_ANI  # Increase animation speed
LED_AND = KC.LED_AND  # Decrease animation speed
LED_MODE_PLAIN = KC.LED_MODE_PLAIN  # LED_M_P	Static LED's
LED_MODE_BREATHE = KC.LED_MODE_BREATHE  # LED_M_B	Breathing animation

# fmt: off
keyboard.keymap = [
    [  #QWERTY
        KC.ESC,     LED_TOG,  LED_INC, LED_ANI, KC.F1,   KC.F2,   KC.F3,  KC.F4, KC.F5, XXXXX, KC.F6,  KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,   KC.BSPC, \
        KC.TAB,     KC.PGUP,  KC.PGDN, KC.GRV,  KC.N1,   KC.N2,   KC.N3,  KC.N4, KC.N5, XXXXX, KC.N6,  KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,   KC.ENT, \
        KC.NUMLOCK, KC.PEQL,  KC.N0,   KC.TAB,  KC.Q,    KC.W,    KC.E,   KC.R,  KC.T,  XXXXX, KC.Y,   KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC,  KC.LSFT, \
        KC.KP_7,    KC.KP_8,  KC.KP_9, KC.CAPS, KC.A,    KC.S,    KC.D,   KC.F,  KC.G,  XXXXX, KC.H,   KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.PIPE,  KC.END, \
        KC.KP_4,    KC.KP_5,  KC.KP_6, KC.LSFT, KC.Z,    KC.X,    KC.C,   KC.V,  KC.B,  XXXXX, KC.N,   KC.M,    KC.UNDS, KC.DOT,  KC.COMM, KC.QUES, KC.HOME,  KC.UP, \
        KC.KP_1,    KC.KP_2,  KC.KP_3, KC.LCTL, KC.LALT, KC.LGUI, KC.SPC, XXXXX, XXXXX, XXXXX, KC.SPC, KC.LGUI, KC.LALT, KC.LCTL, KC.LEFT, KC.DOWN, KC.RIGHT, XXXXX \
    ]
]
# xfmt: on
if __name__ == '__main__':
    keyboard.go()
