import uvicorn
from fastapi import FastAPI
from action import Action

app = FastAPI()

@app.get("/resistor")
async def resistor(r1,r2,r3):
    parallel = (f'Parallel = {float(r1)+float(r2)+float(r3):.2f}')
    serial = (f'serial = {1/float(r1)+1/float(r2)+1/float(r3)**-1:.2f}')
    data = []
    data.append(parallel)
    data.append(serial)
    return data


@app.get("/samakan")
async def samakan(s,t):
    data = (f'V = {float(s)/float(t):.2f}')
    return data

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my_name")
def my_name():
    data ='เป้เองคนสวย'
    return data

@app.get("/Inputmy_name")
def Inputmy_name(name,last_name):
    data ="{} {}".format(name,last_name)
    return data

@app.get("/hw/get")
async def hw_get():
    data = Action.getHW()
    return data

@app.get("/hw/get_by_id")
async def hw_get_by_id(id):
    data = Action.getHWByID(id)
    return data

@app.get("/hw/update")
async def hw_update(id,status,value):
    data = Action.updete(id,status,value)
    return data

@app.post("/users/update")
async def users_update(id,name,last_name):
    data = Action.update_users(id,name,last_name)
    return data

@app.post("/hw/insert")
async def hw_insert(name, hw_name, status,value):
    data = Action.insert_data(name, hw_name, status,value)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)