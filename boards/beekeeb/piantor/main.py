import board
import digitalio
from kb import KMKKeyboard, isRight
from storage import getmount
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.modtap import ModTap
from kmk.handlers.sequences import simple_key_sequence

keyboard = KMKKeyboard()
keyboard.tap_time = 100
keyboard.debug_enabled = True
layers = Layers()

modtap = ModTap()
# optional: set a custom tap timeout in ms
# modtap.tap_time = 300


split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT

data_pin = board.GP1 if split_side == SplitSide.LEFT else board.GP0
data_pin2 = board.GP0 if split_side == SplitSide.LEFT else board.GP1

split = Split(
    split_side=split_side,
    split_type=SplitType.UART,
    split_flip=False,
    data_pin=data_pin,
    data_pin2=data_pin2
)
keyboard.modules = [layers, split]
keyboard.modules.append(modtap)

LOWER = KC.LT(1, KC.SPC)
RAISE = KC.LT(2, KC.TAB)
ADJUST = KC.LT(3, KC.SPC)

#Sequences
AACENT= simple_key_sequence ((KC.GRV,KC.A))
EACENT= simple_key_sequence ((KC.QUOT, KC.MACRO_SLEEP_MS(50), KC.E))
EACENTG= simple_key_sequence ((KC.GRV,KC.E))
EACENTC= simple_key_sequence ((KC.CIRC,KC.E))
IACENTC= simple_key_sequence ((KC.CIRC,KC.I))
OACENTC= simple_key_sequence ((KC.CIRC,KC.O))
CCDILLE= simple_key_sequence ((KC.QUOT,KC.C))
OACENTG= simple_key_sequence ((KC.GRV,KC.O))
USIQUOT= simple_key_sequence ((KC.QUOT,KC.SPC))
USIDQUOT= simple_key_sequence ((KC.DQUO,KC.SPC))
UACENTG= simple_key_sequence (( KC.GRV,KC.U))



# Same as the default Corne/crkbd keymap by foostan and drashna
keyboard.keymap = [
    [  #QWERTY
        KC.ESC,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
        KC.LSFT,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.RSFT,\
        KC.LCTL,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,\
                                        KC.LALT,   KC.MT(KC.SPC, KC.LGUI),  KC.LT(2, KC.TAB),     KC.LT(2, KC.ENT),   LOWER,  KC.TAB,
    ],
    [  #LOWER
        KC.ESC,   KC.N1,   KC.N2, EACENT,  KC.N4, KC.N5,                         KC.PGUP, KC.HOME,   KC.UP,   KC.END,   KC.N0, KC.BSPC,\
        KC.LSFT,  AACENT,  UACENTG, EACENTG, IACENTC, OACENTG,                   KC.PGDN, KC.LEFT, KC.DOWN,   KC.RIGHT, KC.NO,   KC.NO,  \
        KC.LCTL,  CCDILLE, KC.NO, EACENTC, KC.NO,   KC.NO,                       KC.AT,   KC.BSPC,   KC.DQUO, KC.MINS,   KC.NO,   KC.NO,  \
                                        KC.LALT,   KC.MT(KC.SPC, KC.LGUI),  KC.LT(2, KC.TAB),     KC.LT(2, KC.ENT),   LOWER,  KC.TAB,
    ],
    [  #RAISE
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                          KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0, KC.BSPC,\
        KC.LSFT, KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC,                            KC.MINS,  USIDQUOT, KC.LPRN, KC.RPRN, KC.EQUAL,  KC.GRV,\
        KC.LCTL,KC.AMPR,   KC.ASTR,KC.LABK, KC.RABK,KC.BSLASH,                         KC.PLUS, USIQUOT, KC.LBRC, KC.RBRC, KC.BSLS, KC.SLASH, \
                                        KC.LALT, KC.MT(KC.SPC, KC.LGUI), KC.LT(2, KC.TAB), KC.LT(2, KC.ENT), LOWER, KC.TAB,
    ],
    [  #ADJUST
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,                          KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,  \
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,                          KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,  \
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,                          KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO, \
                                    KC.LALT, KC.MT(KC.SPC, KC.LGUI), KC.LT(2, KC.TAB), KC.LT(2, KC.ENT), LOWER, KC.TAB,
    ]
]

if __name__ == '__main__':
    keyboard.go()
