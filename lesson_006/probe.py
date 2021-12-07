class Toyota:

    def __init__(self):
        self.color = "Бордовый металлик"
        self.price = "1 000 000 руб"
        self.max_velocity = "200 км/ч"
        self.current_velocity = "0 км/ч"
        self.engine_rpm = 0

    def start(self):
        self.engine_rpm = 5000

    def go(self):
        self.current_velocity = "20 км/ч"
