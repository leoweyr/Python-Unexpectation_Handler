import datetime

import unexpectation_handler
thisPythonFile = unexpectation_handler.GlobalSymbol(__file__,globals())

def Prompt(time):
    print("[" + time + "]" + "The file already exists!")

def main():
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unexpectation_handler.Handler(thisPythonFile,"open(\"..\\doc\\API reference.md\",\"x\")",0,Prompt,time)

if __name__ == "__main__":
    main()