"""
"
### Image size sample

"""
import TkEasyGUI as eg


def load_image(window, filename):
    # load image and resize
    im: eg.Image = window["-image-"]
    im.update(filename=filename, resize_type=eg.ImageResizeType.FIT_BOTH)

def main():
    # create window
    window = eg.Window(
        "Hello World",
        layout=[
            [eg.Text("Please select an image file")],
            [eg.Input(key="-file-", enable_events=True), eg.FileBrowse()],
            [eg.Image(key="-image-", size=(400, 400), background_color="white")],
            [eg.Button("Close")],
        ],
    )
    load_image(window, "a.jpg")
    # event loop
    while True:
        event, values = window.read()
        print(event, values)
        if event == "-file-":
            filename = values["-file-"]
            load_image(window, filename)
        if event in [eg.WIN_CLOSED, "Close"]:
            break

if __name__ == "__main__":
    main()
