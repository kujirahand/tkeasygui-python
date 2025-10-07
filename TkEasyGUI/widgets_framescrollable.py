"""
A scrollable frame with both vertical and horizontal scrollbars.

[#makedoc:ignore]
"""

import tkinter as tk
from tkinter import ttk


class ScrollableLabelFrame(tk.LabelFrame):
    """A scrollable frame with both vertical and horizontal scrollbars."""

    def __init__(self, master=None, horizontal_scroll=True, **kwargs):
        """Create a scrollable frame with both scrollbars."""
        # Extract width and height if present
        self._width = kwargs.pop("width", None)
        self._height = kwargs.pop("height", None)
        self._horizontal_scroll = horizontal_scroll

        super().__init__(master, **kwargs)

        # キャンバスを作成
        self.canvas = tk.Canvas(self, bg=self.cget("bg"), highlightthickness=0)
        # 垂直スクロールバー（常に表示）
        self.v_scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )
        # 水平スクロールバー（horizontal_scrollの設定に応じて表示）
        self.h_scrollbar = None
        if self._horizontal_scroll:
            self.h_scrollbar = ttk.Scrollbar(
                self, orient="horizontal", command=self.canvas.xview
            )

        # スクロール領域を保持するフレーム
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw"
        )

        # スクロール連動設定
        if self._horizontal_scroll and self.h_scrollbar:
            # 双方向のスクロール連動設定
            self.canvas.configure(
                yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set
            )
        else:
            # 垂直スクロールのみ
            self.canvas.configure(yscrollcommand=self.v_scrollbar.set)

        # 配置
        self.canvas.grid(row=0, column=0, sticky="nsew", padx=8, pady=4)
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")
        if self._horizontal_scroll and self.h_scrollbar:
            self.h_scrollbar.grid(row=1, column=0, sticky="ew")

        # フレームをリサイズ可能に
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Set canvas size if specified
        scrollbar_width = 20 if self.v_scrollbar else 0
        scrollbar_height = 20 if (self._horizontal_scroll and self.h_scrollbar) else 0

        if self._width is not None:
            self.canvas.config(width=self._width - scrollbar_width)
        if self._height is not None:
            self.canvas.config(height=self._height - scrollbar_height)

        # スクロール領域の更新
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        # キャンバスのサイズ変更時に内部フレームをリサイズ
        if self._horizontal_scroll:
            # 水平スクロール有効の場合：幅を調整
            self.canvas.bind(
                "<Configure>",
                lambda e: self.canvas.itemconfig(
                    self.canvas_window,
                    width=max(e.width, self.scrollable_frame.winfo_reqwidth()),
                ),
            )
        else:
            # 水平スクロール無効の場合：キャンバス幅に合わせる
            self.canvas.bind(
                "<Configure>",
                lambda e: self.canvas.itemconfig(
                    self.canvas_window,
                    width=e.width,
                ),
            )

    def get_canvas(self) -> tk.Canvas:
        """Get the canvas widget."""
        return self.canvas
