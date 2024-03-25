"""
Calc sample
"""
import TkEasyGUI as sg

# define the calculator buttons
calc_buttons = [
    ["C", "←", "//", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "%", "="]
]
font = ("Helvetica", 20)
# create window
layout = [
    [sg.Input("0",
             key="-output-", 
             font=font,
             background_color="white",
             color="black",
             readonly_background_color="white",
             readonly=True,
             expand_x=True)],
]
for row in calc_buttons:
    buttons = []
    for ch in row:
        btn = sg.Button(
            ch, # label
            key=f"-btn{ch}",
            size=(3, 1),
            font=font,
        )
        buttons.append(btn)
    layout.append(buttons)
window = sg.Window("Calc", layout)

# event loop
output = "0"
while True:
    event, _ = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    # when a button is pressed
    if event.startswith("-btn"):
        # get label
        ch = window[event].get()
        # clear if text is empty (0 or error)
        if output == "0" or output.startswith("E:"):
            output = ""
        # check label
        if ch == "C": # clear key
            output = "0"
        elif ch == "←": # bs key
            output = output[:-1]
        elif ch == "=": # calc
            try:
                output = str(eval(output))
            except Exception as e:
                output = "E:" + str(e)
        else:
            # add other key
            output += ch
        # update display
        window["-output-"].update(output)
window.close()
