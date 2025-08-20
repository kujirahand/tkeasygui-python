"""
### Image Test
"""

import TkEasyGUI as eg


def main():
    image_files = ["a.jpg", "b.jpg"]
    image_index = 0
    # create window
    window = eg.Window(
        "Image Test",
        layout=[
            [eg.Text("Image:")],
            [
                eg.Image(
                    filename=image_files[0],
                    key="-image-",
                    size=(300, 300),
                    enable_events=True,
                )
            ],
            [eg.Button("Change")],
        ],
    )
    # event loop
    while window.is_running():
        event, values = window.read()
        # print(event, values)
        if event == "Change":
            image_index = (image_index + 1) % len(image_files)
            window["-image-"].update(filename=image_files[image_index])
        if event == "-image-" and values["event_type"] == "mouseup":
            window.post_event("Change", values)


if __name__ == "__main__":
    main()
