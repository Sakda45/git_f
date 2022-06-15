from conDB import con2 

class Action:
    def getHW():
        data = con2.getHW2()
        return data

    def getHWByID(id):
        data = con2.getHWid(id)
        return data

    def updete(id,status,value):
        data = con2.update_hw(id,status,value)
        return data
    
    def update_users(id,name,last_name):
        data = con2.update_users(id,name,last_name)
        return data
    
    def insert_data(name, hw_name, status,value):
        data = con2.insert_data(name, hw_name, status,value)
        return data
