from matplotlib import pyplot as plt

class BaseFuzzy():
    def __init__(self):
        self.maximum = 0
        self.minimum = 0

    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)

    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)


class Temperature(BaseFuzzy):
    def __init__(self):
        self.minimum = -10
        self.maximum = 100

    def freeze(self, x):
        if x >= 0:
            return 1
        else:
            self.minimum = -10
            self.maximum = 0
            return self.up(x)

    def cold(self, x):
        if x <= 0 or x >= 40:
            return 0
        elif 0 < x < 20:
            self.minimum = 0
            self.maximum = 20
            return self.down(x)
        else:
            self.minimum = 20
            self.maximum = 40
            return self.up(x)

    def warm(self, x):
        if x <= 20 or x >= 60:
            return 0
        elif 20 < x < 40:
            self.minimum = 20
            self.maximum = 40
            return self.down(x)
        else:
            self.minimum = 40
            self.maximum = 60
            return self.up(x)

    def hot(self, x):
        if x <= 40:
            return 0
        else:
            self.minimum = 40
            self.maximum = 100
            return self.down(x)


class Pressure(BaseFuzzy):
    def __init__(self):
        self.minimum = 0
        self.maximum = 100

    def very_low(self, x):
        if x >= 0:
            return 1
        else:
            self.minimum = 0
            self.maximum = 10
            return self.up(x)

    def low(self, x):
        if x <= 0 or x >= 40:
            return 0
        elif 0 < x < 20:
            self.minimum = 0
            self.maximum = 20
            return self.down(x)
        else:
            self.minimum = 20
            self.maximum = 40
            return self.up(x)

    def high(self, x):
        if x <= 20 or x >= 60:
            return 0
        elif 20 < x < 40:
            self.minimum = 20
            self.maximum = 40
            return self.down(x)
        else:
            self.minimum = 40
            self.maximum = 60
            return self.up(x)

    def very_high(self, x):
        if x <= 40:
            return 0
        else:
            self.minimum = 40
            self.maximum = 100
            return self.down(x)


class Speed(BaseFuzzy):
    def __init__(self):
        self.minimum = 0
        self.maximum = 100

    def slow(self, x):
        if x >= 0 and x <= 40:
            return 1
        elif x > 40 and x < 60:
            self.minimum = 40
            self.maximum = 60
            return self.down(x)
        else:
            return 0

    def steady(self, x):
        if x <= 40 or x >= 80:
            return 0
        elif 40 < x < 60:
            self.minimum = 40
            self.maximum = 60
            return self.up(x)
        elif 60 <= x <= 80:
            self.minimum = 60
            self.maximum = 80
            return self.down(x)

    def fast(self, x):
        if x <= 60:
            return 0
        elif x > 60 and x < 100:
            self.minimum = 60
            self.maximum = 100
            return self.up(x)
        else:
            return 1


def main(temperature_value, pressure_value):
    speed = Speed()

    speed_value = min(
        speed.fast(Temperature().freeze(temperature_value)) and Pressure().very_low(pressure_value),
        speed.fast(Temperature().cold(temperature_value)) and Pressure().very_low(pressure_value),
        speed.fast(Temperature().warm(temperature_value)) and Pressure().very_low(pressure_value),
        speed.fast(Temperature().hot(temperature_value)) and Pressure().very_low(pressure_value),
        speed.fast(Temperature().freeze(temperature_value)) and Pressure().low(pressure_value),
        speed.steady(Temperature().cold(temperature_value)) and Pressure().low(pressure_value),
        speed.steady(Temperature().warm(temperature_value)) and Pressure().low(pressure_value),
        speed.steady(Temperature().hot(temperature_value)) and Pressure().low(pressure_value),
        speed.steady(Temperature().freeze(temperature_value)) and Pressure().medium(pressure_value),
        speed.steady(Temperature().cold(temperature_value)) and Pressure().medium(pressure_value),
        speed.steady(Temperature().warm(temperature_value)) and Pressure().medium(pressure_value),
        speed.steady(Temperature().hot(temperature_value)) and Pressure().medium(pressure_value),
        speed.steady(Temperature().freeze(temperature_value)) and Pressure().high(pressure_value),
        speed.steady(Temperature().cold(temperature_value)) and Pressure().high(pressure_value),
        speed.steady(Temperature().warm(temperature_value)) and Pressure().high(pressure_value),
        speed.slow(Temperature().hot(temperature_value)) and Pressure().high(pressure_value),
        speed.slow(Temperature().freeze(temperature_value)) and Pressure().very_high(pressure_value),
        speed.slow(Temperature().cold(temperature_value)) and Pressure().very_high(pressure_value),
        speed.slow(Temperature().warm(temperature_value)) and Pressure().very_high(pressure_value),
        speed.slow(Temperature().hot(temperature_value)) and Pressure().very_high(pressure_value)
    )


    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_title('Speed')
    ax.set_xlabel('Speed')
    ax.set_ylabel('Membership')

    # slow
    x_slow = [0, 40, 60, 80, 100]
    y_slow = [1, 1, 0, 0, 0]
    ax.plot(x_slow, y_slow, label='slow')

    # steady
    x_steady = [40, 60, 80, 100, 120]
    y_steady = [0, 1, 1, 0, 0]
    ax.plot(x_steady, y_steady, label='steady')

    # fast
    x_fast = [0, 40, 60, 80, 100, 120]
    y_fast = [0, 0, 0, 0, 1, 1]
    ax.plot(x_fast, y_fast, label='fast')

    ax.legend(loc='upper left')
    ax.set_ylim([-0.1, 1.1])
    ax.set_xticks([0, 40, 60, 80, 100])
    plt.show()


if __name__ == '__main__':
    main(80, 60)
