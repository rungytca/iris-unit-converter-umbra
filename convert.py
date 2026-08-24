"""iris-unit-converter-umbra utility for profile 0012."""
PROJECT = "iris-unit-converter-umbra"
PROFILE = "0012"

def run(value):
    return {"project": PROJECT, "profile": PROFILE, "value": value}

if __name__ == "__main__":
    print(run("ready"))
