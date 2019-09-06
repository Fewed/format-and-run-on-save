from pyautogui import hotkey
from time import sleep
from keyboard import add_hotkey

save_hotkey = 'ctrl s'
safe_save_hotkey = 'ctrl q'
format_hotkey = 'ctrl alt l'
run_hotkey = 'ctrl f5'

format_delay_ms = 100
run_delay_ms = 200
save_delay_ms = 100


def with_hk(str, type=0):
    if type == 0:
        return str.replace(' ', '+')
    return tuple(str.split(' '))


def factory(tup):
    key, delay_ms = tup

    def fun():
        hotkey(*with_hk(key, 1))
        sleep(delay_ms / 1e3)

    return fun


form, run, safe_save = [factory(tup) for tup in [
    (format_hotkey, format_delay_ms),
    (run_hotkey, run_delay_ms),
    (save_hotkey, save_delay_ms)
]]


def format_and_run():
    form()
    run()


# ctrl + q for save
add_hotkey(with_hk(save_hotkey), format_and_run)
# ctrl + s for formatting and save
add_hotkey(with_hk(safe_save_hotkey), safe_save)

input('press any key to exit\n')
