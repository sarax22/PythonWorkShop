#example robot pet!

hunger = 5
energy = 5
happiness = 5

alive = True


def buzzer():
    print("BUZZER: Beep! Your pet needs attention!")


def wag_tail():
    print("Pet wags its tail")


def read_input():
    print("\nAction: feed / play / pet / sleep / quit")
    return input("> ")


def update_pet(action):
    global hunger, energy, happiness

    if action == "feed":
        hunger += 2

    elif action == "play":
        happiness += 2
        energy -= 1

    elif action == "pet":
        wag_tail()
        happiness += 1

    elif action == "sleep":
        energy += 2


def check_pet():
    global alive

    if hunger <= 0 or energy <= 0 or happiness <= 0:
        buzzer()
        print("Your pet is unhappy!")

    if hunger <= -3 or energy <= -3:
        print("Your pet died! ... RIP 😢")
        alive = False


while alive:
    action = read_input()

    if action == "quit":
        break

    update_pet(action)

    hunger -= 1
    energy -= 1

    print("Stats -> Hunger:", hunger, "Energy:", energy, "Happiness:", happiness)

    check_pet()