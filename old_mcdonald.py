def verse(animal, sound):
    print("Old McDonald had a farm")
    print("E-I-E-I-O")
    print("And on that farm he had a", animal)
    print("E-I-E-I-O")
    print("With a", sound, sound, "here")

def main():
    animal_name = input("Animal: ")
    animal_sound = input("Sound: ")
    verse(animal_name, animal_sound)

main()