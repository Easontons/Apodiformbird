print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.sticky_mod import StickyMod
from kmk.modules.encoder import EncoderHandler
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence

# instance keyboard
keyboard = KMKKeyboard()
#keyboard.debug_enabled = True

# keyboard modules
layers = Layers()
holdtap = HoldTap()
sticky_mod = StickyMod()
encoder_handler = EncoderHandler()
combos = Combos()
mouse_keys = MouseKeys()

keyboard.modules = [
    layers,
    holdtap,
    sticky_mod,
    encoder_handler,
    combos,
    mouse_keys
]

# keyboard extensions
media_keys = MediaKeys()
#locks = LockStatus()
rgb = RGB(pixel_pin=board.GP16,
        num_pixels=1,
        val_limit=100,
        hue_default=50,
        sat_default=50,
        rgb_order=(1, 0, 2),  # GRB WS2812
        val_default=10,
        hue_step=5,
        sat_step=5,
        val_step=5,
        animation_speed=1,
        breathe_center=1,  # 1.0-2.7
        knight_effect_length=3,
        animation_mode=AnimationModes.STATIC,
        reverse_animation=False,
        refresh_rate=60,
        )

class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        if self.get_caps_lock():
            rgb.set_hsv_fill(5, 5, 5)
            rgb.set_rgb_fill((102, 0, 0))
            rgb.show()
        else:
            rgb.off()

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Critically important. Do not forget
        if self.report_updated:
            self.set_lock_leds()


locks = LEDLockStatus()
keyboard.extensions = [
    media_keys,
    #locks,
    rgb,
    locks
]

# combos
combos.combos = [
    Chord((5, 6), KC.BSPC, match_coord=True, timeout=25, per_key_timeout=False, fast_reset=False),
]

# 8 cols
keyboard.col_pins = (board.GP29,  # GP29
                     board.GP28,
                     board.GP27,
                     board.GP26,
                     board.GP6,
                     board.GP5,
                     board.GP4,
                     board.GP3)
# 3 rows
keyboard.row_pins = (board.GP11,
                     board.GP10,
                     board.GP9)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# encoder pin
encoder_handler.pins = (
    (board.GP14, board.GP15, None, True),
    (board.GP7,  board.GP8,  None, True),
)


# homerow key
LCTL_A = KC.HT(KC.A, KC.LCTRL, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
LGUI_S = KC.HT(KC.S, KC.LGUI,  prefer_hold=False, tap_interrupted=False, tap_time=500, repeat=HoldTapRepeat.TAP)
LALT_H = KC.HT(KC.H, KC.LALT,  prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
RALT_E = KC.HT(KC.E, KC.RALT,  prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
RGUI_O = KC.HT(KC.O, KC.RGUI,  prefer_hold=False, tap_interrupted=False, tap_time=500, repeat=HoldTapRepeat.TAP)
RCTL_I = KC.HT(KC.I, KC.RCTRL, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)


# shortcut
XXXXXX    = KC.NO
COPY      = KC.SM(kc=KC.C, mod=KC.LCTRL)
PASTE     = KC.SM(kc=KC.V, mod=KC.LCTRL)
UNDO      = KC.SM(kc=KC.Z, mod=KC.LCTRL)
ECD_TAB   = KC.TAB
ECD_STAB  = KC.SM(kc=KC.TAB, mod=KC.LSFT)
#ECD_TAB   = KC.SM(kc=KC.TAB, mod=KC.LALT)
#ECD_STAB  = KC.SM(KC.TAB, KC.LSFT(KC.LALT))

# macro
TABP  =  simple_key_sequence(
    (
     KC.LSFT(no_release=True),
     KC.MACRO_SLEEP_MS(30),
     KC.TAB,
     KC.MACRO_SLEEP_MS(30),
     KC.LSFT(no_press=True)
     )
)

# layers define
ALPHA1    = KC.MO(1)
NUM_SPC   = KC.LT(2, KC.SPC)
SYM1_D    = KC.LT(3, KC.D, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
SYM1_U    = KC.LT(3, KC.U, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
SYM2_R    = KC.LT(4, KC.R, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
SYM2_K    = KC.LT(4, KC.K, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
SYS1_C    = KC.LT(5, KC.C, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
SYS1_L    = KC.LT(5, KC.L, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
CUS1_T    = KC.LT(6, KC.T, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
CUS2_N    = KC.LT(7, KC.N, prefer_hold=False, tap_interrupted=False, tap_time=250, repeat=HoldTapRepeat.TAP)
CUS3_MUTE = KC.LT(8, KC.MUTE, prefer_hold=False, tap_interrupted=False, tap_time=400, repeat=HoldTapRepeat.TAP)
GAME      = KC.TO(9)

# keyboard keymap
keyboard.keymap = [
    #   0          1          2          3          4          5          6          7
    #   KC.NO,     KC.NO,    KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,
    #   XXXXXX,    KC.NO,    KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     XXXXXX,
    #   XXXXXX,    KC.NO,    KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     XXXXXX

    # Layer 0: BASE
    [
        LCTL_A,    LGUI_S,    LALT_H,    CUS1_T,    CUS2_N,    RALT_E,    RGUI_O,    RCTL_I,
        XXXXXX,    SYM1_D,    SYM2_R,    SYS1_C,    SYS1_L,    SYM2_K,    SYM1_U,    XXXXXX,
        XXXXXX,    NUM_SPC,   KC.LSFT,   CUS3_MUTE, GAME,      KC.MEH,    ALPHA1,    XXXXXX
    ],
    # Layer 1: ALPHA1
    [
        KC.Q,      KC.W,      KC.M,      KC.B,      KC.Y,      KC.J,      KC.F,      KC.SCLN,
        XXXXXX,    KC.Z,      KC.X,      KC.V,      KC.G,      KC.P,      KC.NO,     XXXXXX,
        XXXXXX,    KC.SPC,    KC.LSFT,   KC.NO,     KC.NO,     KC.NO,     KC.NO,     XXXXXX
    ],
    # Layer 2: NUMBER
    [
        KC.ESC,    KC.N7,     KC.N8,     KC.N9,     KC.N4,     KC.N5,     KC.N6,     KC.DOT,
        XXXXXX,    KC.LSFT,   KC.DOT,    KC.CAPS,   KC.N1,     KC.N2,     KC.N3,     XXXXXX,
        XXXXXX,    KC.SPC,    KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.N0,     XXXXXX
    ],
    # Layer 3: SYMBOL1
    [
        KC.PPLS,   KC.PMNS,   KC.PAST,   KC.SLSH,   KC.GRV,    KC.TILD,   KC.QUOT,   KC.DQUO,
        XXXXXX,    KC.UNDS,   KC.PIPE,   KC.BSLS,   KC.QUES,   KC.COMM,   KC.DOT,    XXXXXX,
        XXXXXX,    KC.LCTRL,  KC.EQL,    KC.NO,     KC.NO,     KC.EQL,    KC.RCTRL,  XXXXXX
    ],
    # Layer 4: SYMBOL2
    [
        KC.EXLM,   KC.AT,     KC.HASH,   KC.DLR,    KC.LBRC,   KC.LPRN,   KC.RPRN,   KC.RBRC,
        XXXXXX,    KC.PERC,   KC.CIRC,   KC.AMPR,   KC.RCBR,   KC.LABK,   KC.RABK,   XXXXXX,
        XXXXXX,    KC.LCTRL,  KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.LCBR,   XXXXXX
    ],
    # Layer 5: SYSTEM1
    [
        KC.DEL,    KC.PGUP,   KC.INS,    KC.PGDN,   KC.HOME,   KC.UP,     KC.END,    KC.NO,
        XXXXXX,    COPY,      PASTE,     UNDO,      KC.LEFT,   KC.DOWN,   KC.RGHT,   XXXXXX,
        XXXXXX,    KC.TAB,    KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.ENT,    XXXXXX
    ],
    # Layer 6: CUSTOM1
    [
        KC.NO,     KC.NO,    KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,
        XXXXXX,    KC.NO,    KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     XXXXXX,
        XXXXXX,    KC.NO,    KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     XXXXXX
    ],
    # Layer 7: CUSTOM2
    [
        KC.NO,     KC.NO,    KC.MS_UP,   KC.NO,     KC.NO,     KC.MB_LMB, KC.MB_RMB,     KC.NO,
        XXXXXX,    KC.MS_LT, KC.MS_DN,   KC.MS_RT,  KC.NO,     KC.NO,     KC.NO,     XXXXXX,
        XXXXXX,    XXXXXX,   XXXXXX,     XXXXXX,    KC.NO,     KC.NO,     KC.NO,     XXXXXX,
    ],
    # Layer 8: CUSTOM3
    [
        KC.NO,     KC.NO,    KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,
        XXXXXX,    KC.NO,    KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     XXXXXX,
        XXXXXX,    KC.NO,    KC.NO,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     XXXXXX
    ],
    # Layer 9: GAME
    [
        KC.ESC,    KC.NO,    KC.UP,      KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,
        XXXXXX,    KC.LEFT,  KC.DOWN,    KC.RGHT,   KC.NO,     KC.NO,     KC.NO,     XXXXXX,
        XXXXXX,    KC.SPC,   KC.LSFT,    KC.NO,     KC.TO(0),  KC.NO,     KC.NO,     XXXXXX
    ],
]

# encoder map
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU,),      (KC.LSFT(KC.TAB), KC.TAB,)),  # encoder layer 0
    ((KC.VOLD, KC.VOLU,),      (KC.NO, KC.NO,)),  # encoder layer 1
    ((KC.VOLD, KC.VOLU,),      (KC.NO, KC.NO,)),  # encoder layer 2
    ((KC.VOLD, KC.VOLU,),      (KC.NO, KC.NO,)),  # encoder layer 3
    ((KC.VOLD, KC.VOLU,),      (KC.NO, KC.NO,)),  # encoder layer 4
    ((KC.VOLD, KC.VOLU,),      (KC.PGUP, KC.PGDN,)),  # encoder layer 5
    ((KC.VOLD, KC.VOLU,),      (KC.NO, KC.NO,)),  # encoder layer 6
    ((KC.MW_UP, KC.MW_DN,),    (KC.NO, KC.NO,)),  # encoder layer 7
    ((KC.VOLD, KC.VOLU,),      (KC.NO, KC.NO,)),  # encoder layer 8

]

if __name__ == '__main__':
    keyboard.go()
