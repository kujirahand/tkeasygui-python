from PIL import Image
import tkeasygui as sg

def main():
    # load image with Pillow
    def_image = Image.open("a.jpg").resize((400, 400))
    # create window
    window = sg.Window("Hello World", layout=[
        [sg.Text("Hello World")],
        [sg.Image(def_image, key="-image-")],
        [sg.Button("Change")],
        [sg.Button("OK")]
    ])
    # event loop
    while True:
        event, _ = window.read()
        if event == "Change":
            window["-image-"].update(filename="b.jpg")
        if event in [sg.WIN_CLOSED, "OK"]:
            break

if __name__ == "__main__":
    main()
