import tkinter as tk
import ttkbootstrap as ttk

import helper
import manager
import view


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('OBuddyS')
        self.minsize(300, 600)
        self.attributes('-topmost', 1)
        style = ttk.Style()
        style.theme_use("darkly")
        style.colors.primary = style.colors.dark
        self.manager = manager.Manager()
        self.menu = None
        self.song_tracker = view.SongTracker(self, self.manager)
        self.countdown = view.Countdown(self, self.manager)
        self.disclaimer = view.Disclaimer(self, self.manager)
        self.menu = view.Menu(self, self.manager)
        helper.configure_columns(self)
        helper.configure_columns(self.menu)
        helper.configure_columns(self.song_tracker)
        helper.configure_columns(self.countdown)
        helper.configure_columns(self.disclaimer)
        self.menu.grid(column=0, columnspan=12, row=0, sticky=ttk.NSEW, padx=10, pady=10)
        self.song_tracker.grid(column=0, columnspan=12, row=0, sticky=ttk.NSEW, padx=10, pady=10)
        self.countdown.grid(column=0, columnspan=12, row=0, sticky=ttk.NSEW, padx=10, pady=10)
        self.disclaimer.grid(column=0, columnspan=12, row=0, sticky=ttk.NSEW, padx=10, pady=10)
        helper.navigate_to_menu_view(self.menu)


if __name__ == '__main__':
    app = App()
    app.mainloop()
