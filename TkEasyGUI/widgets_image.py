"""Image related functions"""

import io
import sys
import tkinter as tk
from typing import Union

from PIL import Image as PILImage
from PIL import ImageColor, ImageTk

from .utils import ImageResizeType, TkEasyError


# pylint: disable=too-many-arguments, too-many-locals, too-many-positional-arguments, too-many-return-statements, too-many-branches, too-many-statements
def get_image_tk(
    source: Union[bytes, Union[str, None]] = None,
    filename: Union[str, None] = None,
    data: Union[bytes, PILImage.Image, None] = None,
    size: Union[tuple[int, int], None] = None,
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[str, None] = None,  # color (example) "red" or "#FF0000"
) -> Union[ImageTk.PhotoImage, None]:
    """Get Image for tk"""
    img: PILImage.Image
    # if source is bytes, set data
    if source is not None:
        if isinstance(source, str):  # is filename
            filename = source
        else:  # is data
            data = source
    # load from file?
    if filename is not None:
        try:
            img = PILImage.open(filename)
            img = image_resize(
                img,
                size=size,
                resize_type=resize_type,
                background_color=background_color,
            )
            return ImageTk.PhotoImage(image=img)
        except (OSError, ValueError) as e:
            raise TkEasyError(
                f"TkEasyGUI.Image.set_image.Error: filename='{filename}', {e}"
            ) from e
    # load from data
    if data is not None:
        try:
            # check if data is PILImage
            if isinstance(data, PILImage.Image):
                img = data
                img = image_resize(
                    img,
                    size=size,
                    resize_type=resize_type,
                    background_color=background_color,
                )
                return ImageTk.PhotoImage(image=img)
            return ImageTk.PhotoImage(data=data)
        except (tk.TclError, OSError, ValueError, SystemError) as e:
            print("[TkEasyGUI] get_image_tk.Error:", e, file=sys.stderr)
            return None
    return None


def imagedata_to_bytes(image_data: PILImage.Image) -> bytes:
    """Convert JPEG to PNG"""
    bytes_data = io.BytesIO()
    image_data.save(bytes_data, format="PNG")
    img_bytes = bytes_data.getvalue()
    return img_bytes


def imagefile_to_bytes(filename: str) -> bytes:
    """Read image file and convert to bytes"""
    image = PILImage.open(filename)
    bytes_data = io.BytesIO()
    image.save(bytes_data, format="PNG")
    img_bytes = bytes_data.getvalue()
    return img_bytes


def image_resize(
    img: PILImage.Image,
    size: Union[tuple[int, int], None],
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[str, None] = None,  # color (example) "red" or "#FF0000"
) -> PILImage.Image:
    """Resize image"""
    # check background color
    if background_color is None:
        background_color = "white"
    background_color_rgba: int = 0
    c = ImageColor.getcolor(background_color, "RGBA")
    if isinstance(c, int):
        background_color_rgba = c
    if size is None:
        size = img.size
    # resize
    if resize_type == ImageResizeType.NO_RESIZE:
        return img
    if resize_type == ImageResizeType.IGNORE_ASPECT_RATIO:
        return img.resize(size=size)
    if resize_type == ImageResizeType.FIT_HEIGHT:
        r = size[1] / img.size[1]
        w, h = int(img.size[0] * r), size[1]
        x, y = (size[0] - w) // 2, (size[1] - h) // 2
        resize_im = img.resize(size=(w, h))
        view_im = PILImage.new("RGBA", size, background_color_rgba)
        view_im.paste(resize_im, (x, y))
        return view_im
    if resize_type == ImageResizeType.FIT_WIDTH:
        r = size[0] / img.size[0]
        w, h = size[0], int(img.size[1] * r)
        x, y = (size[0] - w) // 2, (size[1] - h) // 2
        resize_im = img.resize(size=(w, h))
        view_im = PILImage.new("RGBA", size, background_color_rgba)
        view_im.paste(resize_im, (x, y))
        return view_im
    if resize_type == ImageResizeType.FIT_BOTH:
        # check aspect ratio
        wr = size[0] / img.size[0]
        hr = size[1] / img.size[1]
        r = min(wr, hr)  # select min
        w, h = int(img.size[0] * r), int(img.size[1] * r)
        x, y = (size[0] - w) // 2, (size[1] - h) // 2
        resize_im = img.resize(size=(w, h))
        view_im = PILImage.new("RGBA", size, background_color_rgba)
        view_im.paste(resize_im, (x, y))
        # print("@@@FIT_BOTH", x, y, w, h, size, wr)
        return view_im
    if resize_type == ImageResizeType.CROP_TO_SQUARE:
        w, h = img.size
        if w > h:
            x = (w - h) // 2
            img = img.crop((x, 0, x + h, h))
        elif h > w:
            y = (h - w) // 2
            img = img.crop((0, y, w, y + w))
        if size is not None:
            img.resize(size=(size[0], size[0]))
    return img
