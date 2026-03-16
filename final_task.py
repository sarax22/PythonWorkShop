"""
FINAL TASK: Robot Pet 🐾

Create an interactive robot pet.

The pet has three needs:
- hunger
- energy
- happiness

If any reach 0, the pet will trigger a buzzer warning.

If needs get too low... your pet might die or run away!
Teams can add their own behaviours.

Team with best Modification will win a prize!
"""


# --- Pet stats ---
hunger = 5
energy = 5
happiness = 5

alive = True


# --- Simulated hardware ---
def buzzer():
    print("BUZZER: Your pet needs attention!")


def wag_tail():
    print("Pet wags its tail happily")


# --- Check pet state ---
def check_pet():
    global alive

    if hunger <= 0 or energy <= 0 or happiness <= 0:
        buzzer()
        print("Your pet is very unhappy!")

    if hunger <= -3 or energy <= -3:
        print("Your pet has died... RIP😢")
        alive = False


# --- Main interaction ---
while alive:

    print("\nChoose action: feed / play / pet / quit")
    action = input("-> ")

    if action == "feed":
        hunger += 2

    elif action == "play":
        happiness += 2
        energy -= 1

    elif action == "pet":
        wag_tail()
        happiness += 1

    elif action == "quit":
        break

    # needs decrease over time
    hunger -= 1
    energy -= 1

    print("Stats → Hunger:", hunger, "Energy:", energy, "Happiness:", happiness)

    check_pet()
