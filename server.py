from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls.reverse()
print(ls)


ls.sort(reverse=True)
print(ls)

ls.sort(key=lambda a: a)
print(ls)

ls.sort(key=lambda a: a, reverse=True)
print(ls)


