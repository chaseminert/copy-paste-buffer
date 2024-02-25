from typing import List

import pyperclip
from keyboard import is_pressed

class Buffer:
    NUM_SLOTS = 9
    empty_list = ["" for _ in range(NUM_SLOTS)]
    FILE_PATH = "Data.txt"
    delim = "$‡@‡$"  # something no one would ever copy

    def __init__(self):
        self._slots: List = Buffer.empty_list

    def set_slot_clipboard(self, slot_num: int) -> None:
        self._slots[slot_num - 1] = pyperclip.paste()

    def set_slot(self, slot_num: int, data: str) -> None:
        self._slots[slot_num - 1] = data

    def clear_all_slots(self) -> None:
        self._slots = Buffer.empty_list

    def print_slots(self) -> None:
        for index, value in enumerate(self._slots):
            print(f"Slot {index + 1}: {value}")
        print()

    def set_clipboard(self, slot_num: int) -> None:
        text: str = self._slots[slot_num - 1]
        pyperclip.copy(text)

    def get_slot(self, slot_num: int) -> str:
        return self._slots[slot_num - 1]

    def save_file(self) -> None:
        if not Buffer._file_exists():
            Buffer._create_file()
        with open(Buffer.FILE_PATH, "w") as file:
            for value in self._slots:
                file.write(f"{value}{Buffer.delim}")

    @staticmethod
    def load_from_file() -> "Buffer":
        delim = Buffer.delim
        if not Buffer._file_exists():
            return Buffer()
        else:
            new_buffer = Buffer()
            with open(Buffer.FILE_PATH, "r") as file:
                file_content = file.read()[:-len(delim)].replace("\n\n", "\n")
            new_buffer._slots = file_content.split(delim)
            return new_buffer

    @staticmethod
    def _file_exists() -> bool:
        try:
            with open(Buffer.FILE_PATH, "r"):
                return True
        except FileNotFoundError:
            return False

    @staticmethod
    def _create_file() -> None:
        with open(Buffer.FILE_PATH, "w", encoding="utf-8") as file:
            file.write("")

    @staticmethod
    def one_to_nine_pressed():
        for i in range(1, Buffer.NUM_SLOTS + 1):
            if is_pressed(str(i)):
                return True, i
        return False, None

    @staticmethod
    def is_valid_copy_press():
        ctrl_alt_pressed = is_pressed("ctrl") and is_pressed("alt")
        zero_to_nine_pressed, key = Buffer.one_to_nine_pressed()
        if ctrl_alt_pressed and zero_to_nine_pressed:
            return True, key
        else:
            return False, None

    @staticmethod
    def is_valid_paste_press():
        ctrl_shift_pressed = is_pressed("ctrl") and is_pressed("shift")
        zero_to_nine_pressed, key = Buffer.one_to_nine_pressed()
        if ctrl_shift_pressed and zero_to_nine_pressed:
            return True, key
        else:
            return False, None

    @staticmethod
    def is_valid_clear_all_slots_input() -> bool:
        return is_pressed("ctrl") and is_pressed("alt") and is_pressed("subtract")

    @staticmethod
    def is_valid_print_input() -> bool:
        return is_pressed("ctrl") and is_pressed("alt") and is_pressed("0")

    @staticmethod
    def is_valid_exit_input() -> bool:
        return is_pressed("ctrl") and is_pressed("shift") and is_pressed("0")
