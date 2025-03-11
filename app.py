import os
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

# Please customize the following variables
USER_NAME = "zfeng6"
VERSION = "1.0.0"

def say_hi(msg:str = "Hi!", file_directory:str = "./output/") -> None:
    # Ensure the output directory exists
    os.makedirs(file_directory, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M")

    # Define filename with timestamp
    file_name = f"outputfile_{USER_NAME}_{VERSION}_timestamp_{timestamp}.txt"
    file_path = os.path.join(file_directory, file_name)

    # Write the timestamp inside the file
    with open(file_path, "w") as file:
        file.write(msg)

    print(f"File '{file_path}' created successfully.")

def add_numbers(a:int, b:int) -> int:
    return a + b

# Add FastAPI Endpoints
@app.get("/")
def read_root():
    """Test API - Confirms FastAPI is running"""
    return {"message": f"Hello, {USER_NAME}!"}

@app.get("/add")
def api_add_numbers(a: int, b: int):
    """API to add two numbers"""
    return {"result": add_numbers(a, b)}

if __name__ == "__main__":
    say_hi()