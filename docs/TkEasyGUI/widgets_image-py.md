# Module TkEasyGUI.widgets_image

Image related functions

---------------------------

- [Functions](#functions-of-tkeasyguiwidgets_image)

# Functions of TkEasyGUI.widgets_image

- [get_image_tk](#get_image_tk)
- [image_resize](#image_resize)
- [imagedata_to_bytes](#imagedata_to_bytes)
- [imagefile_to_bytes](#imagefile_to_bytes)

## get_image_tk

Get Image for tk

```py
def get_image_tk(
    source: Union[bytes, Union[str, None]] = None,
    filename: Union[str, None] = None,
    data: Union[bytes, PILImage.Image, None] = None,
    size: Union[tuple[int, int], None] = None,
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[str, None] = None,  # color (example) "red" or "#FF0000"
) -> Union[ImageTk.PhotoImage, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_image.py#L15)

## image_resize

Resize image

```py
def image_resize(
    img: PILImage.Image,
    size: Union[tuple[int, int], None],
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[str, None] = None,  # color (example) "red" or "#FF0000"
) -> PILImage.Image:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_image.py#L83)

## imagedata_to_bytes

Convert JPEG to PNG

```py
def imagedata_to_bytes(image_data: PILImage.Image) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_image.py#L66)

## imagefile_to_bytes

Read image file and convert to bytes

```py
def imagefile_to_bytes(filename: str) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_image.py#L74)

