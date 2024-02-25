import time

from buffer import Buffer
from utils import ClipboardUtils

TIME_DELAY_SECS = 0.25  # an upper bound for the time a key will be pressed down
TIME_SHORT_DELAY_SECS = 0.01  # the time between loops (implemented for performance reasons)


def main():
    print("Copy To Slot     --->   CTRL + ALT + <any number 1-9>")
    print("Paste From Slot  --->   CTRL + SHIFT + <any number 1-9>")
    print("Clear All        --->   CTRL + ALT + <minus key>")
    print("Print All        --->   CTRL + ALT + 0")
    print("Exit And Save    --->   CTRL + SHIFT + 0\n")

    slot_buffer = Buffer.load_from_file()

    while True:
        is_valid_copy_press, copy_key = Buffer.is_valid_copy_press()
        if is_valid_copy_press:
            ClipboardUtils.copy_from_screen()
            slot_buffer.set_slot_clipboard(copy_key)

        is_valid_paste_press, paste_key = Buffer.is_valid_paste_press()
        if is_valid_paste_press:
            slot_buffer.set_clipboard(paste_key)
            ClipboardUtils.paste_to_screen()

        if Buffer.is_valid_clear_all_slots_input():
            slot_buffer.clear_all_slots()
            time.sleep(TIME_DELAY_SECS)
            print("All slots have been cleared")

        if Buffer.is_valid_print_input():
            print("Slot values:")
            slot_buffer.print_slots()
            time.sleep(TIME_DELAY_SECS)

        if Buffer.is_valid_exit_input():
            slot_buffer.save_file()
            exit(0)

        time.sleep(TIME_SHORT_DELAY_SECS)


if __name__ == "__main__":
    main()
