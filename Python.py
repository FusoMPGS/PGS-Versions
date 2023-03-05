# Copy and Paste all this code into a IDE and save it as a HEX File or Download V1 from the Github Page
def Creation():
    for index in range(2):
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . .
                        . # . . .
                        . . . . .
        """)
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
        basic.show_leds("""
            # . . . .
                        . # . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . .
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
    basic.clear_screen()
    basic.pause(200)
    basic.show_string("Rithul")

def on_logo_long_pressed():
    Creation()
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    global rps_Input
    rps_Input = randint(0, 3)
    basic.pause(2000)
    if rps_Input == 1:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    elif rps_Input == 2:
        basic.show_leds("""
            # # . # #
                        # # . # .
                        . . # . .
                        # # . # .
                        # # . . #
        """)
    else:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    pass
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_pin_pressed_p2():
    radio.send_string("ok")
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_gesture_screen_down():
    radio.send_string("no")
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    radio.send_string("Call?")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    music.play_melody("B A G A G F A C5 ", 120)
    music.set_built_in_speaker_enabled(True)
    if input.button_is_pressed(Button.B):
        while input.is_gesture(Gesture.LOGO_DOWN):
            music.stop_all_sounds()
            basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global rand_Tempo
    music.play_melody("D F G A F A B C5 ", randint(135, 220))
    rand_Tempo += 1
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_down():
    basic.show_number(input.temperature())
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

rand_Tempo = 0
rps_Input = 0
rps_Input = 0
radio.set_group(119)
