import serial
import tkinter


def change_servo_position(device: serial, label: tkinter.Label, servo_number: int, operation: str) -> None:
    """
    Функция меняет положение сервопривода.

    Последовательность действий:
    1) В зависимости от операции вызвать функцию уменьшающую, либо увеличивающую счётчик.
    2) Вызвать функцию, которая меняет положение сервопривода на текущее (уменьшенное или увеличенное).

    :param device:          последовательный порт, к которому подключена плата Arduino
    :param label:           виджет, отображающий текст (отсчитывает угол поворота сервопривода)
    :param servo_number:    номер сервопривода (от 1 до 6), который необходимо покрутить
    :param operation:       код операции ("+" или "-")
    """
    pass


def increment(label: tkinter.Label) -> int:
    """
    Функуия увеличивает значение угла поворота сервопривода.

    Последовательность действий:
    1) Получить текущее значение угла.
    2) Проверить, не превосходит ли оно 180.
    3) Увеличить его на значение шага (брать равным 20).

    :param label:           виджет, отображающий текст (отсчитывает угол поворота сервопривода)
    :return:                новое значение угла
    """
    pass


def decrement(label: tkinter.Label) -> int:
    """
    Функуия уменьшает значение угла поворота сервопривода.

    Последовательность действий:
    1) Получить текущее значение угла.
    2) Проверить, что оно не равно нулю.
    3) Уменьшить его на значение шага (брать равным 20).

    :param label:           виджет, отображающий текст (отсчитывает угол поворота сервопривода)
    :return:                новое значение угла
    """
    pass


def send_data(device: serial, line: str) -> None:
    """
    Функция отправляет строку на последовательный порт Arduino.

    :param device:          последовательный порт, к которому подключена плата Arduino
    :param line:            команда
    """
    line += "\r\n"
    device.write(line.encode())


def move_servo(device: serial, servo_number: int, new_value: int) -> None:
    """
    Функция меняет положение сервопривода на заданное.

    Последовательность действий:
    1) Отправить на Arduino команду, сформированную из входных данных.

    Общий вид команды: s[SERVO_NUMBER][ANGLE]
    Примеры команд: s2100, s180, s5140

    :param device:          последовательный порт, к которому подключена плата Arduino
    :param servo_number:    номер сервопривода (от 1 до 6), который необходимо покрутить
    :param new_value:       значение угла, которое необходимо установить
    """
    pass


if __name__ == "__main__":
    arduino = serial.Serial("/dev/ttyUSB0", 10100)
    servo_id = 1

    root = tkinter.Tk()
    root.geometry("300x200")
    root.title("Управление сервоприводом")
    root.resizable(0, 0)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

    servo_angle = tkinter.Label(root, text="100")

    minus_button = tkinter.Button(
        root,
        text="-",
        command=lambda x=servo_id: change_servo_position(arduino, servo_angle, x + 1, "-")
    )

    plus_button = tkinter.Button(
        root,
        text="+",
        command=lambda x=servo_id: change_servo_position(arduino, servo_angle, x + 1, "+")
    )

    i = 0
    for element in minus_button, servo_angle, plus_button:
        element.grid(column=i, row=0, sticky=tkinter.EW)
        i += 1

    root.mainloop()
