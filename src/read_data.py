import json

def get_person_data():
    """
    Returns the person data loaded from the JSON file.
    """
    
    # Opening JSON file
    file = open("data/person_db.json")

    # Loading the JSON File in a dictionary
    person_data = json.load(file)

    return person_data


def get_person_names():
    """
    Returns a list of person names from the loaded person data.
    """
    # gib mir die Liste mit allen Personen
    persons_dict = get_person_data()
    names_list = []
    # gehe durch die Liste
    for person_data in persons_dict:
        # jeder Eintrag ist ein Dictionary mit den Feldern (firstname, lastname)
        names_list.append(person_data["lastname"] + ", " + person_data["firstname"])
        # hänge das an die Namensliste an
    return names_list

def get_person_data_by_name(personname):
    all_persons = get_person_data()
    lastname, firstname = personname.split(", ")
    
    for person_data in all_persons:
        if person_data["firstname"] == firstname and person_data["lastname"] == lastname:
            return person_data # dictionary einer Person


def get_person_image_by_name(personname):
    picture_path = get_person_data_by_name(personname)["picture_path"]
    return picture_path  # gibt den Pfad zum Bild zurück

if __name__ == "__main__":
    # Example usage
    person_data = get_person_data()
    print(person_data)
    person_names = get_person_names()
    print(person_names)
    person_name = "Huber, Julian"
    person_dict = get_person_data_by_name(person_name)
    print(person_dict)
    get_person_image_by_name(person_name)
    print(get_person_image_by_name(person_name))