from pyfirmata import Arduino
import time

# sesuaikan komunikasi serial anda,
# disini saya mendapatkan COM4
board = Arduino("COM4")

while True:
    board.digital[5].write(1)
    time.sleep(0.2)
    board.digital[5].write(0)
    time.sleep(0.2)
    board.digital[6].write(1)
    time.sleep(0.2)
    board.digital[6].write(0)
    time.sleep(0.2)
    board.digital[7].write(1)
    time.sleep(0.2)
    board.digital[7].write(0)
    time.sleep(0.2)