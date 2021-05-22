class Auto:
    autp_count = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        Auto.autp_count += 1


ferrari = Auto(35, 'red')

print(ferrari.color)