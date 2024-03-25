"""
TkEasyGUI dialogs
"""
import platform
import subprocess
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from datetime import datetime, timedelta
from tkinter import colorchooser
from typing import Any

import TkEasyGUI as eg

#------------------------------------------------------------------------------
# Dialogs
#------------------------------------------------------------------------------
# like PySimpleGUI

def popup_buttons(message: str, title: str = "Question", buttons: list[str] = ["OK", "Cancel"], 
        auto_close_duration: int = -1, timeout_key: str="-TIMEOUT-", non_blocking: bool = False) -> str:
    """
    Popup window with user defined buttons. Return button's label.

    #### Example:
    ```py
    color = eg.popup_buttons(
        "Which color do you like?", 
        "Question",
        buttons=["red","yellow","green"])
    print(color)
    ```
    """
    result = buttons[-1] if len(buttons) > 0 else None
    # create window
    win = eg.Window(title, layout=[
        [eg.Text(message)],
        [eg.Button(s, width=9) for s in buttons],
    ], modal=True)
    # event loop
    timer_id = eg.time_checker_start()
    autoclose_sec: int = auto_close_duration * 1000
    if non_blocking:
        # TODO: popup non blocking window
        pass
    while win.is_alive():
        event, _ = win.read(timeout=100, timeout_key=eg.WINDOW_TIMEOUT)
        if event in buttons:
            result = event
            break
        if event == eg.WINDOW_TIMEOUT:
            if auto_close_duration > 0 and eg.time_checker_end(timer_id) > autoclose_sec:
                result = timeout_key # timeout_key only use result
                break
    win.close()
    return result

def popup(message: str, title: str = "") -> str:
    """
    Display a message in a popup window.
    
    #### Example:
    ```py
    eg.popup("I like an apple.", "Information")
    ```
    """
    # messagebox.showinfo(title, message)
    return popup_buttons(message=message, title=title, buttons=["OK"])

def popup_non_blocking(message: str, title: str="", auto_close_duration: int = -1) -> str:
    """(TODO) Display a non blocking window"""
    return popup_buttons(message, title, buttons=["OK"], auto_close_duration=auto_close_duration, non_blocking=True)

def popup_no_buttons(message: str, title: str="") -> None:
    popup_buttons(message, title, buttons=[])

def popup_auto_close(message: str, title: str="", auto_close_duration: int = 3, buttons: list[str] = ["OK", "Cancel"], timeout_key="-TIMEOUT-") -> str:
    """Display a message in a popup window that closes automatically after a specified time."""
    return popup_buttons(message, title, buttons=buttons, auto_close_duration=auto_close_duration, timeout_key=timeout_key)

def popup_no_wait(message: str, title: str="", **kw) -> str:
    """Display a message in a popup window without waiting."""
    return popup_auto_close(message, title, auto_close_duration=0, **kw)

def popup_ok(message: str, title: str="") -> str:
    """Display a message in a popup window.(Alias popup)"""
    return popup_buttons(message, title, buttons=["OK"])

def popup_ok_cancel(message: str, title: str="") -> str:
    """Display a message in a popup window with OK and Cancel buttons. Return "OK" or "Cancel"."""
    return popup_buttons(message, title, buttons=["OK", "Cancel"])

def popup_yes_no(message: str, title: str = "Question", yes_label: str="Yes", no_label: str="No") -> str:
    """
    Display a message in a popup window with Yes and No buttons. Return "Yes" or "No".

    #### Example:
    Ask user question, [Yes] or [No]
    ```py
    a = eg.popup_yes_no("Do you like Sushi?", "Question")
    print(a) # "Yes" or "No"
    ```
    Ask user question in Japanes [はい] or [いいえ]
    ```py
    ja_a = eg.popup_yes_no("寿司は好き?", "質問", yes_label="はい", no_label="いいえ")
    print(ja_a) # "はい" or "いいえ"
    ```
    """
    # return "Yes" if messagebox.askyesno(title, message) else "No"
    return popup_buttons(message, title, buttons=[yes_label, no_label])

def popup_yes_no_cancel(message: str, title: str = "Question") -> str:
    """Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" or "Cancel"."""
    return popup_buttons(message, title, buttons=["Yes", "No", "Cancel"])

def popup_cancel(message: str, title: str="") -> str:
    """Display a message in a popup window with OK and Cancel buttons. Return "OK" or "Cancel"."""
    return popup_buttons(message, title, buttons=["Cancel"])

def popup_get_text(message: str, title: str = "", default: str = "", font: tuple[Any]|None=None) -> (str|None):
    """Display a message in a popup window with a text entry. Return the text entered."""
    # return simpledialog.askstring(title, message, initialvalue=default)
    return popup_input(message, title, default, font=font)

def popup_input(message: str, title: str = "", default: str = "", font: tuple[Any]|None=None) -> (str|None):
    """Display a message in a popup window with a text entry. Return the text entered."""
    result = None
    win = eg.Window(title, layout=[
        [eg.Text(message)],
        [eg.Input(default, key="-user-", width=40)],
        [eg.Button("OK", width=9), eg.Button("Cancel", width=9)]
    ], modal=True, font=font)
    while win.is_alive():
        event, values = win.read()
        if event == "OK":
            result = values["-user-"]
            break
        if event == "Cancel":
            break
    win.close()
    return result

def popup_error(message: str, title: str="Error") -> None:
    """Display a message in a popup window with an error icon."""
    popup_buttons(message, title, buttons=["Error"])
    # messagebox.showerror(title, message)

def popup_warning(message: str, title: str="Warning") -> None:
    """Display a message in a popup window with an warning icon."""
    messagebox.showwarning(title, message)

def popup_info(message: str, title: str="Warning") -> None:
    """Display a message in a popup window with an warning icon."""
    messagebox.showwarning(title, message)

def popup_get_file(message: str="", title: str|None=None, initial_folder: str="", save_as: bool=False, multiple_files: bool=False, file_types: tuple[tuple[str, str]]=(("All Files", "*.*"),), no_window: bool|None=None, **kw) -> (str|tuple[str]|None):
    """Popup a file selection dialog. Return the file selected."""
    if title is None:
        title = message
    if save_as:
        result = filedialog.asksaveasfilename(
            title=title,
            initialdir=initial_folder,
            filetypes=file_types,
            **kw)
    else:
        result = filedialog.askopenfilename(
            title=title, 
            initialdir=initial_folder,
            filetypes=file_types,
            multiple=multiple_files, # type: ignore
            **kw)
    return result

def popup_get_folder(message: str="", title: str|None=None, default_path: str="", no_window: bool|None=None, **kw) -> (str|None):
    """Popup a folder selection dialog. Return the folder selected."""
    if title is None:
        title = message
    return filedialog.askdirectory(title=title, initialdir=default_path, **kw)

def popup_scrolled(message: str, title: str = "", size: tuple[int,int]=[40, 5], readonly: bool=False, font: tuple[str, int]|None=None) -> str|None:
    """Display a message in a popup window with a text entry. Return the text entered."""
    win = eg.Window(title, layout=[
        [eg.Multiline(message, key="-text-", size=size, readonly=readonly, font=font)],
        [eg.Button("OK", width=9), eg.Button("Cancel", width=5)]
    ], modal=True)
    result = None
    while win.is_alive():
        event, _ = win.read()
        if event == "OK":
            result = win["-text-"].get()
            break
        if event == "Cancel":
            break
    win.close()
    return result

def popup_get_date(message: str = "", title: str = "", current_date:datetime|None=None, font: tuple[str, int]|None=None) -> datetime|None:
    """Display a calendar in a popup window. Return the datetime entered or None."""
    if current_date is None:
        current_date = datetime.now()
    # week names
    week_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    week_colors = [None, None, None, None, None, "blue", "red"]
    # set
    result = None
    layout = []
    # header
    if message != "":
        layout.append([eg.Text(message)])
        layout.append([eg.HSeparator()])
    # select month
    month_button = [
        eg.Button("←", key="-prev-"),
        eg.Button(f"{current_date.year:04}-{current_date.month:02}-{current_date.day:02}", key="-ymd-", size=[10,1]),
        eg.Button("→", key="-next-"),
        eg.Button("▲", key="-today-"),
    ]
    layout.append(month_button)
    week_buttons = [
        eg.Button(name, size=[2,1], disabled=True, text_color=week_colors[i])
        for i, name in enumerate(week_names)]
    layout.append(week_buttons)
    # get top left day
    def get_top_date(current: datetime) -> datetime:
        # Return day of the week, where Monday == 0 ... Sunday == 6.
        first_day: datetime = datetime(year=current.year, month=current.month, day=1)
        week_i:int = first_day.weekday()
        top_date = first_day
        if week_i >= 1:
            top_date = first_day - timedelta(days=week_i)
        return top_date
    cols = []
    cur = get_top_date(current_date)
    for i in range(35):
        cols.append(eg.Button(
            cur.day, size=[2,1], key=f"-b{i}-",
            text_color=week_colors[i%7],
            disabled=(current_date.month != cur.month)))
        if i % 7 == 6:
            layout.append(cols)
            cols = []
        cur = cur + timedelta(days=1)
    layout.append([eg.HSeparator()])
    layout.append([
        # eg.Text(f"{current_date.year}-{current_date.month}-{current_date.day}", key="-result-"), 
        # eg.Text("|"),
        eg.Button("OK"), eg.Button("Cancel")])
    # update label
    def update_date(top: datetime, current_date: datetime):
        cur = datetime(year=top.year, month=top.month, day=top.day)
        for i in range(35):
            btn: eg.Button = window[f"-b{i}-"]
            # selected
            selected = current_date.month == cur.month and current_date.day == cur.day
            # todo: change color?
            # fg = "green" if selected else week_colors[i%7]
            # bg = "blue" if selected else "white"
            # update
            btn.set_text(cur.day if not selected else f"*{cur.day}*")
            btn.set_disabled(current_date.month != cur.month)
            # btn.update(text_color=fg, background_color=bg)
            cur = cur + timedelta(days=1)
        window["-ymd-"].update(f"{current_date.year:04}-{current_date.month:02}-{current_date.day:02}")
    # update result
    def update_result(current_date):
        top = get_top_date(datetime(year=current_date.year, month=current_date.month, day=1))
        update_date(top, current_date)
    # calendar window
    window = eg.Window(title, layout, font=font, modal=True)
    result = None
    while window.is_alive():
        event, _ = window.read()
        if event == "OK":
            result = current_date
            break
        elif event == "Cancel":
            result = None
            break
        elif event == "-today-":
            current_date = datetime.now()
            update_date(get_top_date(current_date), current_date)
        elif event == "-prev-":
            y, m = current_date.year, current_date.month - 1
            if m == 0:
                y -= 1
                m = 12
            current_date = datetime(year=y, month=m, day=1)
            update_date(get_top_date(current_date), current_date)
        elif event == "-next-":
            y, m = current_date.year, current_date.month + 1
            if m == 13:
                y += 1
                m = 1
            current_date = datetime(year=y, month=m, day=1)
            update_date(get_top_date(current_date), current_date)
        elif event.startswith("-b"):
            elm:eg.Button = window[event]
            label = str(elm.get_text()).replace("*", "")
            current_date = datetime(year=current_date.year, month=current_date.month, day=int(label))
            update_result(current_date)
    window.close()
    return result

#------------------------------------------------------------------------------
# for notify
def popup_notify(message: str, title: str="") -> None:
    """Popup a information"""
    if is_mac():
        send_notification_mac(message, title)
    elif is_win():
        send_notification_win(message, title)
    else:
        popup_buttons(message, title, buttons=["OK"], auto_close_duration=1)

def send_notification_mac(message: str, title: str=""):
    """"Send Notification on mac"""
    if title == "":
        title = "Notification"
    script = 'display notification "{}" with title "{}"'.format(message, title)
    subprocess.run(['osascript', '-e', script])

def send_notification_win(message: str, title: str=""):
    """"Send Notification on win"""
    msg = message.replace("'@", "' @")
    if title != "":
        title = title.replace("'@", "' @")
        msg = f"{title}\n{msg}"
    powershell_script = fr'''
$bodyText = @'
{title}
{message}
'@
$ToastText01 = [Windows.UI.Notifications.ToastTemplateType, Windows.UI.Notifications, ContentType = WindowsRuntime]::ToastText01
$TemplateContent = [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]::GetTemplateContent($ToastText01)
$TemplateContent.SelectSingleNode('//text[@id="1"]').InnerText = $bodyText
$AppId = '{{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}}\WindowsPowerShell\v1.0\powershell.exe'
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($AppId).Show($TemplateContent)
'''
    # Execute PowerShell
    subprocess.run(["powershell", "-Command", powershell_script])

#------------------------------------------------------------------------------
# TkEasyGUI original dialogs

def popup_color(title: str="", default_color: str|None=None) -> (str|None):
    """Popup a color selection dialog. Return the color selected."""
    col = colorchooser.askcolor(title=title, color=default_color)
    if col[1] is None:
        return default_color
    return f"{col[1]}".upper()

def popup_listbox(items: list[str], message: str = "", title: str = "", size: tuple[int,int]=(20, 7), font: tuple[str, int]|None=None, multiple:bool = False) -> str|None:
    """Display Listbox in a popup window"""
    select_mode = eg.LISTBOX_SELECT_MODE_BROWSE if multiple is False else eg.LISTBOX_SELECT_MODE_MULTIPLE
    win = eg.Window(title, layout=[
        [eg.Text(message)],
        [eg.Listbox(values=items, key="-list-", size=size, font=font, select_mode=select_mode)],
        [eg.Button("OK", width=9), eg.Button("Cancel", width=5)]
    ], modal=True)
    result = None
    while win.is_alive():
        event, _ = win.read()
        if event == "Cancel":
            result = None
            break
        if event == "OK":
            selected = win["-list-"].get()
            if multiple:
                result = selected
            else:
                if len(selected) == 1:
                    result = selected[0]
            break
    win.close()
    return result

#------------------------------------------------------------------------------
# TKinter
def ask_yes_no(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with Yes and No buttons. Return True or False. (use Tkinter)"""
    return messagebox.askyesno(title, message)

def ask_ok_cancel(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with OK and Cancel buttons. Return True or False. (use Tkinter)"""
    return messagebox.askokcancel(title, message)

def ask_retry_cancel(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with Retry and Cancel buttons. Return True or False. (use Tkinter)"""
    return messagebox.askretrycancel(title, message)

def show_message(message: str, title: str="Information") -> None:
    """show message in a popup window"""
    messagebox.showinfo(title, message)

def show_info(message: str, title: str="Information") -> None:
    """show message in a popup window"""
    messagebox.showinfo(title, message)

def msgbox(message: str, title: str="Message") -> None:
    """show message in a popup window like VB"""
    messagebox.showinfo(title, message)

#------------------------------------------------------------------------------
# utility
def get_platform() -> str:
    """get platform"""
    return platform.system()

def is_mac() -> bool:
    """platform : is mac?"""
    return get_platform() == "Darwin"
def is_win() -> bool:
    """platform : is Windows?"""
    return get_platform() == "Windows"
