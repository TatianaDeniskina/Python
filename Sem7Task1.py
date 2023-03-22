from time import sleep
from datetime import datetime as dt


class TrafficLight:
    """ Класс светофора, реализующий свое переключение при запуске running( """
    _states = {'red': 7, 'yellow': 2, 'green': 7}
    _color = ''

    def running(self):
        """ Метод запусключения светофора """
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"Светофор приведен в состояние  '{self._color}' "
                  f"на {sw_time} секунд")

            sleep(sw_time)

            print(f"Светофор покидает режим  '{self._color}' после "
                  f"{(dt.now() - start_state_time).seconds} секунд")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()