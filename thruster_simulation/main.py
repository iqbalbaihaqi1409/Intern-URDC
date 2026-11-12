
class Thruster:
    def __init__(self, name):
        self.name = name
        self.output = 0

    def set_output(self, value):
        # Membatasi output dari -100 sampai 100
        self.output = max(-100, min(100, value))

    def stop(self):
        self.output = 0


class ASVController:
    def __init__(self):
        # Membuat 4 object thruster
        self.FL = Thruster("FL")
        self.FR = Thruster("FR")
        self.RL = Thruster("RL")
        self.RR = Thruster("RR")

        self.thrusters = [self.FL, self.FR, self.RL, self.RR]
        self.status = "STOP"

    def forward(self, speed):
        for thruster in self.thrusters:
            thruster.set_output(speed)

        self.status = "FORWARD"

    def backward(self, speed):
        for thruster in self.thrusters:
            thruster.set_output(-speed)

        self.status = "BACKWARD"

    def turn_left(self, turn_value=30):
        self.FL.set_output(-turn_value)
        self.FR.set_output(turn_value)
        self.RL.set_output(-turn_value)
        self.RR.set_output(turn_value)

        self.status = "TURN LEFT"

    def turn_right(self, turn_value=30):
        self.FL.set_output(turn_value)
        self.FR.set_output(-turn_value)
        self.RL.set_output(turn_value)
        self.RR.set_output(-turn_value)

        self.status = "TURN RIGHT"

    def stop(self):
        for thruster in self.thrusters:
            thruster.stop()

        self.status = "STOP"

    def emergency_stop(self):
        self.stop()
        self.status = "EMERGENCY STOP"

    def display_status(self):
        print("\n===== STATUS ASV =====")
        print("Gerakan:", self.status)

        for thruster in self.thrusters:
            print(f"{thruster.name}: {thruster.output}")

        print("======================")


def main():
    asv = ASVController()

    while True:
        print("\n================================")
        print("     SIMULASI 4 THRUSTER ASV")
        print("================================")
        print("1. Forward")
        print("2. Backward")
        print("3. Turn Left")
        print("4. Turn Right")
        print("5. Stop")
        print("6. Emergency Stop")
        print("7. Exit")
        print("================================")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            try:
                speed = int(input("Masukkan kecepatan (0-100): "))

                if 0 <= speed <= 100:
                    asv.forward(speed)
                    asv.display_status()
                else:
                    print("Error: Kecepatan harus 0-100!")

            except ValueError:
                print("Error: Input harus berupa angka!")

        elif pilihan == "2":
            try:
                speed = int(input("Masukkan kecepatan (0-100): "))

                if 0 <= speed <= 100:
                    asv.backward(speed)
                    asv.display_status()
                else:
                    print("Error: Kecepatan harus 0-100!")

            except ValueError:
                print("Error: Input harus berupa angka!")

        elif pilihan == "3":
            asv.turn_left()
            asv.display_status()

        elif pilihan == "4":
            asv.turn_right()
            asv.display_status()

        elif pilihan == "5":
            asv.stop()
            asv.display_status()

        elif pilihan == "6":
            asv.emergency_stop()
            asv.display_status()

        elif pilihan == "7":
            asv.stop()
            print("Program simulasi ASV selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih 1-7.")


if __name__ == "__main__":
    main()
