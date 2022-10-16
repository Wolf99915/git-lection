from models.models import Toyota

while True:
    print("Create your Toyota\n" +
        "1. Create new Toyota\n" +
        "2. Get all Toyota\n" +
        "3. Change color Toyota by ID\n" +
        "4. Driving\n"
        )

    flag = int(input("Chose menu ithem: "))
    if flag == 1:
        model = input("Toyota model: ")
        engine = input("Toyota engine: ")
        color = input("Toyota color: ")
        toyota = Toyota(model, engine, color)
        toyota.save()
    elif flag == 2:
        Toyota.get_all_toyota()
    elif flag == 3:
        id = int(input("Type id to search: "))
        Toyota.update(id)
    elif flag == 4:
        print("start riding =)")
        Toyota.drive()
        