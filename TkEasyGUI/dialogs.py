"""
TkEasyGUI dialogs
"""
import os
import subprocess
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from datetime import datetime, timedelta
from tkinter import colorchooser
from typing import Any, Callable, Iterable, Optional, Union

from . import locale_easy as le
from . import widgets as eg
from .utils import ColorFormatType, FontType, get_root_window, is_mac, is_win

YES = "Yes"
NO = "No"
OK = "OK"
CANCEL = "Cancel"

# save original print
_print = print

#------------------------------------------------------------------------------
# Dialogs
#------------------------------------------------------------------------------
# like PySimpleGUI

def popup_buttons(
        message: str,
        title: Union[str,None] = None,
        buttons: list[str] = ["OK", "Cancel"], 
        auto_close_duration: int = -1, # auto close duration (msec)
        timeout_key: str="-TIMEOUT-", # timeout key
        non_blocking: bool = False,
        default: str = '',
    ) -> str:
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
    if title is None:
        title = le.get_text("Question")
    result = buttons[-1] if len(buttons) > 0 else default

    # create window
    eg_buttons: list[eg.Element] = [eg.Button(s, width=9) for s in buttons]
    eg_buttons_pad: list[eg.Element] = [eg.Push()] + eg_buttons + [eg.Push()]
    layout: eg.LayoutType = [
        [eg.Text(message)],
        eg_buttons_pad,
    ]
    
    # event loop
    timer_id = eg.time_checker_start()
    autoclose_sec: int = auto_close_duration * 1000
    if non_blocking:
        # TODO: popup non blocking window
        pass
    with eg.Window(title, layout=layout, modal=True) as win:
        for event, _ in win.event_iter(timeout=100, timeout_key=eg.WINDOW_TIMEOUT):
            if event in buttons:
                result = event
                break
            if event == eg.WINDOW_TIMEOUT:
                if auto_close_duration > 0 and eg.time_checker_end(timer_id) > autoclose_sec:
                    result = timeout_key # timeout_key only use result
                    break
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
    """Display a message in a popup window without buttons."""
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

def popup_ok_cancel(
        message: str,
        title: Union[str,None] = None,
        ok_label: Union[str, None] = None,
        cancel_label: Union[str, None] = None,
        ok_value: str = "OK",
        cancel_value: str = "Cancel",
        ) -> str:
    """Display a message in a popup window with OK and Cancel buttons. Return "OK" or "Cancel" or eg.WINDOW_CLOSED."""
    if ok_label is None:
        ok_label = le.get_text("OK")
    if cancel_label is None:
        cancel_label = le.get_text("Cancel")
    result = popup_buttons(message, title, buttons=[ok_label, cancel_label])
    if result == ok_label:
        return ok_value
    if result == cancel_label:
        return cancel_value
    return result # pushed close button

def popup_yes_no(
                message: str, # question message
                title: Union[str,None] = None, # window title
                yes_label: Union[str,None]=None, # label for yes button
                no_label: Union[str,None]=None, # label for no button
                yes_value: str = "Yes", # return value for yes
                no_value: str = "No" # return value for no
                ) -> str:
    """
    Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" (or eg.WINDOW_CLOSED).
    @see [tests/localize_test.py](https://github.com/kujirahand/tkeasygui-python/blob/main/tests/localize_test.py)
    #### Example - simple:
    Ask user question, [Yes] or [No] buttons.
    ```py
    ans = eg.popup_yes_no("Do you like Sushi?", "Question")
    print(ans) # "Yes" or "No"
    ```
    #### Eample - custom label:
    Ask user question in special button
    ```py
    ans = eg.popup_yes_no("Do you eat Sushi?", yes_label="EAT", no_label="no")
    print(ans) # "Yes" or "No"
    ```
    #### Example - custom return value:
    ans = eg.popup_yes_no("Can you speak Japanese?", yes_value="can", no_value="no")
    print(ans) # "can" or "no"
    """
    # get locale text
    title = title if title is not None else le.get_text("Question")
    yes_label = yes_label if yes_label is not None else le.get_text("Yes")
    no_label = no_label if no_label is not None else le.get_text("No")
    # ask yes or no
    result = popup_buttons(message, title, buttons=[yes_label, no_label])
    # get result
    if result == yes_label:
        return yes_value
    if result == no_label:
        return no_value
    return result # pushed close button

def popup_yes_no_cancel(
        message: str,
        title: Union[str, None] = None,
        yes_label: Union[str, None] = None,
        no_label: Union[str, None] = None,
        cancel_label: Union[str, None] = None,
        yes_value: str = "Yes",
        no_value: str = "No",
        cancel_value: str = "Cancel"
        ) -> str:
    """Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" or "Cancel"."""
    # return popup_buttons(message, title, buttons=["Yes", "No", "Cancel"])
    # get locale text
    title = title if title is not None else le.get_text("Question")
    yes_label = yes_label if yes_label is not None else le.get_text("Yes")
    no_label = no_label if no_label is not None else le.get_text("No")
    cancel_label = cancel_label if cancel_label is not None else le.get_text("Cancel")
    # ask yes or no
    result = popup_buttons(message, title, buttons=[yes_label, no_label, cancel_label])
    # get result
    if result == yes_label:
        return yes_value
    if result == no_label:
        return no_value
    if result == cancel_label:
        return cancel_value
    return cancel_label

def popup_cancel(message: str, title: str="") -> str:
    """Display a message in a popup window with OK and Cancel buttons. Return "Cancel" or eg.WINDOW_CLOSED."""
    cancel_label = le.get_text("Cancel")
    result = popup_buttons(message, title, buttons=["Cancel"])
    return cancel_label if result == cancel_label else result

def popup_get_text(
        message: str,
        title: Union[str,None] = None,
        default: Union[str, None] = None,
        default_text: Union[str, None] = None, # same as default for compatibility
        font: Optional[FontType]=None) -> Union[str, None]:
    """Display a message in a popup window with a text entry. Return the text entered."""
    # return simpledialog.askstring(title, message, initialvalue=default)
    if default_text is not None:
        default = default_text
    default_str = ''
    if default is not None:
        default_str = default
    result: Union[str, float, None] = popup_input(
        message, title, default_str, font=font
    )
    if result is None:
        return None
    return str(result)

def popup_input(
    message: str,
    title: Optional[str] = None,
    default: str = "",
    ok_label: Optional[str] = None,
    cancel_label: Optional[str] = None,
    cancel_value: Any = None,
    only_number: bool = False,
    font: Optional[FontType] = None,
) -> Union[str, float, None]:
    """Display a message in a popup window with a text entry. Return the text entered. if canceled, return cancel_value."""
    result = cancel_value
    if title is None:
        title = le.get_text("Text input") if only_number is False else le.get_text("Number input")
    if ok_label is None:
        ok_label = le.get_text("OK")
    if cancel_label is None:
        cancel_label = le.get_text("Cancel")
    win = eg.Window(title, layout=[
        [eg.Text(message)],
        [eg.Input(default, key="-user-", width=40, enable_events=True)],
        [eg.Button(ok_label, width=11), eg.Button(cancel_label, width=9)]
    ], modal=True, font=font)
    while True:
        event, values = win.read()
        if (event == ok_label) or ((event == "-user-") and (values["event_type"] == "return")):
            result = values["-user-"]
            if only_number:
                try:
                    result = float(result)
                except ValueError as _:
                    popup(le.get_text("Please enter a number."))
                    continue
            break
        if event in [cancel_label, eg.WINDOW_CLOSED]:
            # let result = cancel_value
            break
    win.close()
    return result

def popup_error(message: str, title: Union[str,None]=None) -> None:
    """Display a message in a popup window with an error icon."""
    if title is None:
        title = le.get_text("Error")
    error_label = le.get_text("Error")
    popup_buttons(message, title, buttons=[error_label])
    # messagebox.showerror(title, message)

def popup_warning(message: str, title: Union[str,None]=None) -> None:
    """Display a message in a popup window with an warning icon."""
    if title is None:
        title = le.get_text("Warning")
    messagebox.showwarning(title, message)

def popup_info(message: str, title: Union[str,None]=None) -> None:
    """Display a message in a popup window with an warning icon."""
    if title is None:
        title = le.get_text("Information")
    messagebox.showwarning(title, message)

def popup_get_file(
        message: str="",
        title: Union[str, None] = None,
        initial_folder: Union[str, None] = None,
        save_as: bool = False, # show `save as` dialog
        multiple_files: bool = False, # can select multiple files
        file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
        default_extension: Union[str, None] = None,
        no_window: Union[bool, None] = None, # for compatibility
        **kw) -> Union[str, tuple[str], None]:
    """Popup a file selection dialog. Return the file selected."""
    if title is None:
        title = message
    if initial_folder is None:
        initial_folder = os.getcwd()
    file_type_list: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = []
    if file_types is not None:
        # check file types
        new_types = []
        for ft in file_types:
            if len(ft) != 2:
                ft = (ft, ft)
            # fix file types for mac (#52)
            # like ("Image Files", *.jpg;*.jpeg;*.jpe;*.heic")
            if is_mac():
                if ";" in ft[1]:
                    desc = ft[0]
                    exts = ft[1].split(";")
                    for ext in exts:
                        new_types.append((desc, ext))
                    continue
            new_types.append(ft)
        file_type_list = tuple(new_types)
    if save_as:
        result = filedialog.asksaveasfilename(
            title=title,
            initialdir=initial_folder,
            filetypes=file_type_list,
            defaultextension=default_extension,
        )
        if result and default_extension:
            if result.endswith(default_extension) is False:
                result += default_extension
    else:
        result = filedialog.askopenfilename(
            title=title,
            initialdir=initial_folder,
            filetypes=file_type_list,
            multiple=multiple_files,  # type: ignore
            **kw,
        )
    return result

def popup_get_folder(
            message: str = "",
            title: Union[str, None] = None,
            default_path: Union[str, None] = None,
            no_window: Union[bool, None] = None, # for compatibility
            **kw
            ) -> Union[str, None]:
    """Popup a folder selection dialog. Return the folder selected."""
    if title is None:
        title = message
    if default_path is None:
        default_path = os.getcwd()
    return filedialog.askdirectory(title=title, initialdir=default_path, **kw)

def popup_memo(
        message: str,
        title: Union[str, None] = None,
        size: tuple[int,int] = (60, 8),
        readonly: bool = False,
        ok_label: Union[str, None] = None,
        cancel_label: Union[str, None] = None,
        cancel_value: Union[str,None] = None,
        font: Union[FontType, None] = None
        ) -> Union[str, None]:
    """Display a multiline message in a popup window. Return the text entered. if canceled, return cancel_value."""
    return popup_scrolled(message, title, size, readonly, ok_label, cancel_label, cancel_value, font)

def popup_scrolled(
    message: str,
    title: Optional[str] = None,
    size: tuple[int, int] = (40, 5),
    readonly: bool = False,
    ok_label: Optional[str] = None,
    cancel_label: Optional[str] = None,
    cancel_value: Optional[str] = None,
    font: Optional[FontType] = None,
) -> Union[str, None]:
    """
    Display a multiline message in a popup window. Return the text entered. if canceled, return cancel_value.
    #### Example:
    ```py
    import TkEasyGUI as eg
    text = eg.popup_scrolled("This is a long text.", "Information")
    eg.print(text)
    ```
    """
    result = cancel_value
    if cancel_label is None:
        cancel_label = le.get_text("Cancel")
    if ok_label is None:
        ok_label = le.get_text("OK")
    title_str: str = ''
    if title is None:
        title_str = le.get_text("Information")
    layout: eg.LayoutType = [
        [eg.Multiline(message, key="-text-", size=size, readonly=readonly, font=font)],
        [eg.Button(ok_label, width=9), eg.Button(cancel_label, width=5)],
    ]
    win: eg.Window = eg.Window(title=title_str, layout=layout, modal=True)
    result = None
    while win.is_alive():
        event, _ = win.read()
        if event == ok_label:
            result = win["-text-"].get()
            break
        if event == cancel_label:
            break
    win.close()
    return result

def popup_get_date(
        message: str = "",
        title: Union[str, None] = None,
        current_date: Union[datetime, None] = None,
        font: Union[tuple[str, int], None] = None,
        ok_label: Union[str, None] = None,
        cancel_label: Union[str, None] = None,
        date_format: Union[str, None] = None,
        close_when_date_chosen: bool = False,
        sunday_first: bool = False, # Sunday is the first day of the week
        ) -> Union[datetime, None]:
    """Display a calendar in a popup window. Return the datetime entered or None."""
    if current_date is None:
        current_date = datetime.now()
    if date_format is None:
        date_format = le.get_text("__date_format__", "%Y-%m-%d")
    date_format_str: str = date_format
    if title is None:
        title = le.get_text("Select date")
    # week names
    week_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    week_colors = ["black", "black", "black", "black", "black", "blue", "red"]
    if sunday_first:
        week_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        week_colors = ["red", "black", "black", "black", "black", "black", "blue"]
    days_size = [4, 1]
    head_size = [4, 1]
    # set
    result = None
    layout: eg.LayoutType = []
    # header
    if message != "":
        layout.append([eg.Text(message)])
        layout.append([eg.HSeparator()])
    # select month
    month_button: list[eg.Element] = [
        eg.Frame(
            "",
            layout=[
                [
                    eg.Button("ᐊ", key="-prev2-", padx=0, size=(1, 1)),
                    eg.Button("◀", key="-prev-", padx=0, size=(1, 1)),
                    eg.Button(current_date.strftime(date_format_str), key="-ymd-", size=(10, 1)),
                    eg.Button("▶", key="-next-", padx=0, size=(1, 1)),
                    eg.Button("ᐅ", key="-next2-", padx=0, size=(1, 1)),
                ]
            ],
            expand_x=True,
            text_align="center",
            relief="flat",
            pady=[2, 4],
        )
    ]
    layout.append(month_button)
    week_labels: list[eg.Element] = [
        eg.Text(
            name,
            size=head_size,
            text_color=week_colors[i],
            text_align="center",
            # background_color="white",
            padx=2,
            pady=1,
            color=week_colors[i],
        )
        for i, name in enumerate(week_names)
    ]
    layout.append(week_labels)
    # get top left day
    def get_top_date(current: datetime) -> datetime:
        # Return day of the week, where Monday == 0 ... Sunday == 6.
        first_day: datetime = datetime(year=current.year, month=current.month, day=1)
        week_i:int = first_day.weekday()
        top_date = first_day
        if sunday_first:
            # Sunday first
            if week_i != 6:
                top_date = first_day - timedelta(days=week_i + 1)
        else:
            # Monday first
            if week_i >= 1:
                top_date = first_day - timedelta(days=week_i)
        return top_date
    # create calendar days buttons
    cols: list[eg.Element] = []
    cur = get_top_date(current_date)
    for i in range(42):
        cols.append(
            eg.Text(
                f"{cur.day}",
                size=days_size,
                key=f"-b{i}-",
                text_color=week_colors[i % 7],
                background_color="white",
                text_align="center",
                enable_events=True,
                disabled=(current_date.month != cur.month),
                padx=2,
                pady=1,
                metadata={"date": datetime.fromtimestamp(cur.timestamp())}
            )
        )
        if i % 7 == 6:
            layout.append(cols)
            cols = []
        cur = cur + timedelta(days=1)
    layout.append([eg.HSeparator()])
    # ok, cancel buttons
    if ok_label is None:
        ok_label = le.get_text("OK")
    if cancel_label is None:
        cancel_label = le.get_text("Cancel")
    panel = eg.Frame(
        "",
        layout=[
            [
                eg.Button(ok_label, size=(10, 1)),
                eg.Button(cancel_label, size=(8, 1)),
            ]
        ],
        text_align="center",
        expand_x=True,
        relief="flat",
    )
    layout.append([panel])
    # update label
    def update_date(top: datetime, current_date: datetime):
        cur = datetime(year=top.year, month=top.month, day=top.day)
        for i in range(42):
            btn: eg.Text = window[f"-b{i}-"]
            fg = week_colors[i%7]
            bg = "white"
            # selected
            selected = current_date.month == cur.month and current_date.day == cur.day
            if selected:
                fg = "red"
                bg = "#aaeeff"
                if i % 7 == 6:
                    fg = "black"
            # update
            btn.set_text(str(cur.day))
            btn.set_disabled(current_date.month != cur.month)
            btn.update(text_color=fg, background_color=bg)
            if btn.metadata is not None:
                btn.metadata["date"] = datetime.fromtimestamp(cur.timestamp())
            # next day
            cur = cur + timedelta(days=1)
        window["-ymd-"].update(current_date.strftime(date_format_str))
    # update result
    def update_result(current_date):
        top = get_top_date(datetime(year=current_date.year, month=current_date.month, day=1))
        update_date(top, current_date)
    result = None
    # calendar window
    with eg.Window(title, layout, font=font, modal=True, row_padding=0) as window:
        for event, _ in window.event_iter():
            if event == ok_label:
                result = current_date
                break
            elif event == cancel_label:
                result = None
                break
            elif event == "-today-" or event == "-ymd-":
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
            elif event == "-prev2-":
                y, m  = current_date.year - 1, current_date.month
                current_date = datetime(year=y, month=m, day=1)
                update_date(get_top_date(current_date), current_date)
            elif event == "-next2-":
                y, m = current_date.year + 1, current_date.month
                current_date = datetime(year=y, month=m, day=1)
                update_date(get_top_date(current_date), current_date)
            elif event.startswith("-b"):
                elm:eg.Text = window[event]
                if elm is None or elm.metadata is None:
                    continue
                sel_date: datetime = elm.metadata["date"]
                if sel_date.month == current_date.month:
                    current_date = sel_date
                    update_result(current_date)
                    if close_when_date_chosen:
                        result = current_date
                        break
                else:
                    current_date = sel_date
                    update_date(get_top_date(current_date), current_date)
    return result

def popup_get_form(
    form_items: list[Union[str, tuple[str, Any], tuple[str, Any, str]]], # list of form items(label[,selection or default][,type])
    title: str = "Form" # window title
) -> Union[dict[str, Any], None]:
    """
        Displays a form that allows multiple items to be entered.
        By specifying the labels and input types for each item, the form is automatically generated and displayed in a dialog.
        When the user enters the items and clicks [OK], it returns `{label: value}`. If the user clicks [Cancel], it returns `None`.

        The `form_items` argument can specify input fields simply as `[label1, label2, label3, ...]`.
        Alternatively, you can specify labels, types, and default values as `[(label1, default1, type1), (label2, default2, type2), ...]`.
        The following values can be specified for the type: `text`, `number`, `password`, `combo`, `list`, `date`, `file`, `files`, `folder`, `color`.

        @see [tests/popup_get_form_test.py](/tests/popup_get_form_test.py)

        #### Simple Example:
        ```py
        import TkEasyGUI as eg
        form = eg.popup_get_form(["Name", "Hobbies"])
        if form:
            name = form["Name"]
            hobbies = form["Hobbies"]
            eg.print(f"name={name}, hobbies={hobbies}")
        ```

        #### Example:
        ```py
        import TkEasyGUI as eg
        result = eg.popup_get_form([
            # [label, default_or_selections, type]
            ["Name", "Suzu", "text"],
            ["Age", 20, "number"],
            ["Hobbies", ["Reading", "Writing"], "list"],
            ["OS", ["Windows", "macOS", "Ubuntu"], "combo"],
            ["Password", "", "password"],
            ["Date", "", "date"],
            ["File", "", "file"],
            ["Folder", "", "folder"],
            ["Theme Color", "", "color"],
        ])
        if result:
            print(result)
        ```
    """
    # make form layout
    item_labels = []
    item_converters: list[Union[Callable, None]] = []
    layout: eg.LayoutType = []
    for i, it in enumerate(form_items):
        it_key = f"-formitem{i}"
        if isinstance(it, tuple) or isinstance(it, list):
            label = it[0]
            default_value = it[1] if len(it) >= 2 else ""
            itype = it[2] if len(it) >= 3 else "text"
            if isinstance(default_value, tuple) or isinstance(default_value, list):
                itype = "list"
        else:
            label = it
            default_value = ""
            itype = "text"
        if itype == "":
            itype = "text"
        # for making result
        item_labels.append(label)
        item_converters.append(None)
        # make line
        line: list[eg.Element] = [eg.Text(label, key=f"{it_key}-label", size=(15, 1), text_align="right")]
        # check type
        itype = itype.lower()
        if itype == "text" or itype == "number" or itype == "password":
            line.append(eg.Input(
                default_value, key=it_key, size=(20, 1),
                password_char="*" if itype == "password" else None))
            if itype == "number":
                item_converters[i] = float
        elif itype == "combo":
            sels = default_value
            val = sels[0] if len(sels) > 0 else ""
            line.append(eg.Combo(sels, default_value=val, key=it_key, size=(19, 1)))
        elif itype == "list":
            sels = default_value
            val = sels[0] if len(sels) > 0 else ""
            line.append(eg.Input(val, key=it_key, size=(15, 1)))
            line.append(eg.ListBrowse(sels))
        elif itype == "date":
            line.append(eg.Input(default_value, key=it_key, size=(15, 1)))
            line.append(eg.CalendarBrowse())
        elif itype == "file":
            line.append(eg.Input(default_value, key=it_key, size=(15, 1)))
            line.append(eg.FileBrowse())
        elif itype == "files":
            line.append(eg.Input(default_value, key=it_key, size=(15, 1)))
            line.append(eg.FileBrowse(multiple_files=True))
        elif itype == "folder":
            line.append(eg.Input(default_value, key=it_key, size=(15, 1)))
            line.append(eg.FolderBrowse())
        elif itype == "color":
            line.append(eg.Input(default_value, key=it_key, size=(15, 1)))
            line.append(eg.ColorBrowse())
        # append line
        layout.append(line)
    layout.append([eg.HSeparator()])
    cancel_label = le.get_text("Cancel")
    layout.append([eg.Push(), eg.Button("OK", width=9), eg.Button(cancel_label, key="Cancel", width=5), eg.Push()])
    with eg.Window(title, layout=layout) as win:
        result: Union[dict[str, Any], None] = None
        for event, values in win.event_iter():
            if event == "Cancel":
                result = None
                break
            if event == "OK":
                result = {}
                for i, label in enumerate(item_labels):
                    it_key = f"-formitem{i}"
                    val = values[it_key] if it_key in values else ""
                    fn = item_converters[i]
                    try:
                        if fn is not None:
                            val = fn(val)
                    except ValueError as _:
                        popup(le.get_text("Please enter a number."))
                        win.focus_element(it_key)
                        result = None
                        break
                    result[label] = val
                # form error?
                if result is None:
                    continue
                break
    return result

#------------------------------------------------------------------------------
# for notify
#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------

def popup_color(
    title: str = "",
    default_color: Union[str, None] = None,
    format: ColorFormatType = "html",
) -> Union[str, tuple[int,int,int], None]:
    """
    Popup a color selection dialog. Return the color selected.
    format: "html", "rgb", "tuple"
    """
    col = colorchooser.askcolor(title=title, color=default_color)
    if col[1] is None:
        return default_color
    html = col[1].upper()
    if format == "html":
        return html
    elif format == "rgb":
        return html[1:]
    elif format == "tuple":
        return col[0]
    return html

def popup_listbox(
    values: list[str],  # list of items
    message: str = "",
    title: str = "",
    size: tuple[int, int] = (20, 7),
    font: Union[FontType, None] = None,
    default_value: Union[str, None] = None,  # default value
    multiple: bool = False,  # multiple selection
) -> Union[str, None]:
    """Display Listbox in a popup window"""
    select_mode: eg.ListboxSelectMode = eg.LISTBOX_SELECT_MODE_BROWSE if multiple is False else eg.LISTBOX_SELECT_MODE_MULTIPLE
    # create window
    layout: list[list[eg.Element]] = []
    if message != "":
        layout.append([eg.Text(message)])
    layout.append([
        eg.Listbox(
            values=values, key="-list-",
            default_value=default_value, size=size,
            font=font, select_mode=select_mode
        )])
    layout.append([eg.Button("OK", width=9), eg.Button("Cancel", width=5)])
    with eg.Window(title, layout=layout, modal=True) as win:
        # event loop
        result = None
        for event, values in win.event_iter():
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
    return result

def popup_image(
        message: str,
        title: Union[str,None] = None,
        image_path: Union[str,None] = None,
        image_data: Union[bytes,None] = None,
        size: tuple[int,int] = (400, 300),
        ok_label: Union[str, None] = None,
        ok_value: str = "OK",
        cancel_label: Union[str, None] = None,
        cancel_value: Union[str, None] = None,
        font: Union[FontType, None] = None,
        ) -> Union[str, None]:
    """Display an image in a popup window. Return the pushed Button("OK" or None)."""
    if title is None:
        title = message
    if ok_label is None:
        ok_label = le.get_text("OK")
    if cancel_label is None:
        cancel_label = le.get_text("Cancel")
    layout: list[list[eg.Element]] = [
        [eg.Text(message)],
        [eg.Image(image_path, image_data, size=size)],
        [eg.Button(ok_label, width=9), eg.Button(cancel_label, width=5)],
    ]
    win = eg.Window(title, layout=layout, modal=True, font=font)
    result = cancel_value
    while win.is_alive():
        event, _ = win.read()
        if event == ok_label:
            result = ok_value
            break
        if event == cancel_label:
            break
    win.close()
    return result


#------------------------------------------------------------------------------
# TKinter alias
#------------------------------------------------------------------------------
def ask_yes_no(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with Yes and No buttons. Return True or False. (use Tkinter)"""
    return messagebox.askyesno(title, message)

def ask_ok_cancel(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with OK and Cancel buttons. Return True or False. (use Tkinter)"""
    return messagebox.askokcancel(title, message)

def ask_retry_cancel(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with Retry and Cancel buttons. Return True or False. (use Tkinter)"""
    return messagebox.askretrycancel(title, message)

def show_message(
        message: str,
        title: Union[str,None] = None
    ) -> None:
    """show message in a popup window"""
    title = title if title is not None else le.get_text("Information")
    messagebox.showinfo(title, message)

def show_info(
        message: str,
        title: Union[str,None] = None
    ) -> None:
    """show message in a popup window"""
    title = title if title is not None else le.get_text("Information")
    messagebox.showinfo(title, message)

def msgbox(
        message: str, # message
        title: Union[str,None] = None
    ) -> None:
    """show message in a popup window like VB"""
    title = title if title is not None else le.get_text("Information")
    messagebox.showinfo(title, message)

#------------------------------------------------------------------------------
# TkEasyGUI original dialogs
#------------------------------------------------------------------------------
def input(
        message: str,
        title: Union[str,None] = None,
        default: str = "",
        only_number: bool = False
    ) -> Union[str, float, None]:
    """Display a message in a popup window with a text entry. Return the text entered."""
    return popup_input(message, title, default, only_number=only_number)

def print(*args, **kw) -> None:
    """Print message to popup window.(call default print function if no_window is True)"""
    if "no_window" in kw and kw["no_window"]:
        _print(*args)
        return
    lines = " ".join([str(a) for a in args])
    popup(lines)

def input_number(
        message: str,
        title: Union[str,None] = None,
        default: str = ""
    ) -> Union[float, None]:
    """Display a message in a popup window with a number entry. Return the text entered."""
    result = popup_input(message, title, default, only_number=True)
    if isinstance(result, float):
        return result
    return None

def confirm(
        question: str,
        title: Union[str,None] = None
    ) -> bool:
    """Display a message in a popup window with Yes and No buttons. Return True or False."""
    return popup_yes_no(question, title, yes_value="Yes") == "Yes"

#------------------------------------------------------------------------------
# To prevent the display of an empty window
_ = get_root_window()
