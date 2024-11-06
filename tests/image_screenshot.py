# screenshot sample
import TkEasyGUI as eg


def main():
    # create window
    window = eg.Window(
        "Screenshot App",
        layout=[
            [eg.Image(key="-image-", filename="a.jpg", size=(400, 400), background_color="white")],
            [eg.Button("Screenshot"), eg.Button("Close")],
        ],
    )
    # event loop
    while True:
        event, values = window.read()
        print(event, values)
        if event in [eg.WIN_CLOSED, "Close"]:
            break
        if event == "Screenshot":
            image: eg.Image = window["-image-"]
            screen_img = image.screenshot()
            window.post_event("Screenshot:done", {"image": screen_img})
        if event == "Screenshot:done":
            fname = eg.popup_get_file(
                "Save screenshot as:", save_as=True, default_extension=".png"
            )
            if fname:
                screen_img.save(fname)
            print("Screenshot done")

if __name__ == "__main__":
    main()
