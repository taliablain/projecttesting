
def user_input():
    dog_size = input("what size is your dog? ")
    dog_energy = input("how energetic is your dog? ")
    exercise_classes = ["yoga", "zumba", "obstacle course", "dog fun run"]
    return dog_size, dog_energy

def give_recommendation(dog_size, dog_energy):

    if dog_energy == "lazy":
        recommendation = "yoga"
        print(recommendation)

    if dog_energy == "moderate":
        recommendation = "zumba"
        print(recommendation)

    if dog_energy == "active":
        recommendation = "obstacle course"
        print(recommendation)

    if dog_size == "small":
        amount = "once a week"
        print(amount)

    if dog_size == "medium":
        amount = "twice a week"
        print(amount)

    if dog_size == "large":
        amount = "three times a week"
        print(amount)


give_recommendation(*user_input())