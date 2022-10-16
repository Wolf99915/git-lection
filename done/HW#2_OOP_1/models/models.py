import json

class Toyota:
    file = "models.json"

    def __init__(self, model, engine, color):
        self.model = model
        self.engine = engine
        self.color = color

    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file, "r")
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_toyota(cls):
        data = cls.get_data()
        for toyota in data:
            print("_______________\n")
            print('model: ', toyota["model"])
            print('engine volume: ', toyota["engine"])
            print('color: ', toyota["color"])
            print('ID: ', toyota["id"])
            print("_______________\n")

    @classmethod
    def get_by_id(cls, id):
        counter = 0
        toyotas = cls.get_data()
        for toyota in toyotas:
            if id == toyota['id']:
                print("_______________\n")
                print('You select toyota: ', toyota["model"])
                print('engine volume: ', toyota["engine"])
                print('color: ', toyota["color"])
                print("_______________\n")
                break
            counter+=1
            if counter == len(toyotas):
                print('Not found Toyota with this id')

    # change paint for car in file json
    @classmethod
    def update(cls, id):
        counter = 0
        paints = cls.get_data()
        for paint in paints:
            if id == paint['id']:
                print("_______________\n")
                print('Active color: ', paint["color"])
                new_color = input("enter new color: ")
                paint["color"] = new_color
                print('new color: ', paint["color"])
                print("_______________\n")
                break
            counter+=1
            if counter == len(paints):
                print('Not found Toyota with this id')
        file = open("database/" + cls.file, "w")
        data_in_json = json.dumps(paints)
        file.write(data_in_json)
        

    @classmethod
    def gear_shift(cls):
        gear = int(input('Select gear: '))
        if gear <= 0:
            print('We can`t go ')
            print("_______________\n")
        elif gear >= 6:
            print('gear is so high')
            print("_______________\n")
        else:
            print('Gear ', gear,' selected')
    
    @classmethod
    def drive(cls):
        while True:
            print(
            "1. Keep on driving\n" +
            "2. Stop\n" +
            "3. Shift gear\n"
            )
            flag = int(input("Chose menu ithem: "))
            if flag == 1:
                print('We are still driving')
                print("_______________\n")
            elif flag == 2:
                print('Stop')
                print("_______________\n")
                break
            elif flag == 3:
                Toyota.gear_shift()

                

   
    def save(self):
        data = self.get_data()
        new_toyota = {"model": self.model, "engine": self.engine, "color": self.color}
        if len(data) > 0:
            new_toyota["id"] = data[-1]["id"] + 1
        else:
            new_toyota["id"] = 1
        data.append(new_toyota)
        file = open("database/" + self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)