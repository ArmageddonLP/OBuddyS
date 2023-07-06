from abc import ABC, abstractmethod

import ttkbootstrap as ttk

import helper


class Menu(ttk.Frame):
    def __init__(self, window, manager):
        super().__init__(window)
        self.window = window
        self.manager = manager
        self.refresh()

    def item(self, row, view, name):
        ttk.Label(self, text=name, font=("Helvetica", 14)).grid(column=0, columnspan=11, row=row, sticky=ttk.NSEW)
        ttk.Button(self, text="EDIT", command=lambda: helper.navigate_to_crud_view(view, name)).grid(column=11, columnspan=1, row=row)
        row += 1
        helper.separator(self, row)
        row += 1
        return row

    def refresh(self):
        for widget in self.winfo_children():
            widget.destroy()
        row = 0
        self.title = ttk.Label(self)
        self.title["text"] = "MAIN MENU"
        self.title["font"] = "Helvetica", 18
        self.title.grid(column=0, columnspan=12, row=row)
        row += 1
        helper.separator(self, row)
        row += 1
        self.song_trackers = ttk.Label(self)
        self.song_trackers["text"] = "SONG TRACKERS"
        self.song_trackers["font"] = "Helvetica", 16
        self.song_trackers.grid(column=0, columnspan=11, row=row, sticky=ttk.NSEW)
        self.add_song_tracker_button = ttk.Button(self)
        self.add_song_tracker_button["text"] = "ADD"
        self.add_song_tracker_button["command"] = lambda: helper.navigate_to_crud_view(self.window.song_tracker, "")
        self.add_song_tracker_button.grid(column=11, columnspan=1, row=row)
        row += 1
        helper.separator(self, row)
        row += 1
        for name in self.manager.get_state()[self.manager.SONG_TRACKERS].keys():
            row = self.item(row, self.window.song_tracker, name)
        self.countdowns = ttk.Label(self)
        self.countdowns["text"] = "COUNTDOWNS"
        self.countdowns["font"] = "Helvetica", 16
        self.countdowns.grid(column=0, columnspan=11, row=row, sticky=ttk.NSEW)
        self.add_countdown_button = ttk.Button(self)
        self.add_countdown_button["text"] = "ADD"
        self.add_countdown_button["command"] = lambda: helper.navigate_to_crud_view(self.window.countdown, "")
        self.add_countdown_button.grid(column=11, columnspan=1, row=row)
        row += 1
        helper.separator(self, row)
        row += 1
        for name in self.manager.get_state()[self.manager.COUNTDOWNS].keys():
            row = self.item(row, self.window.countdown, name)
        self.disclaimers = ttk.Label(self)
        self.disclaimers["text"] = "DISCLAIMERS"
        self.disclaimers["font"] = "Helvetica", 16
        self.disclaimers.grid(column=0, columnspan=11, row=row, sticky=ttk.NSEW)
        self.add_disclaimer_button = ttk.Button(self)
        self.add_disclaimer_button["text"] = "ADD"
        self.add_disclaimer_button["command"] = lambda: helper.navigate_to_crud_view(self.window.disclaimer, "")
        self.add_disclaimer_button.grid(column=11, columnspan=1, row=row)
        row += 1
        helper.separator(self, row)
        row += 1
        for name in self.manager.get_state()[self.manager.DISCLAIMERS].keys():
            row = self.item(row, self.window.disclaimer, name)


class AbstractCRUDView(ttk.Frame, ABC):
    def __init__(self, window, manager):
        super().__init__(window)
        self.window = window
        self.manager = manager
        self.refresh("")

    @abstractmethod
    def refresh(self, name):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def cancel(self):
        pass


class SongTracker(AbstractCRUDView):
    def __init__(self, window, manager):
        super().__init__(window, manager)

    def refresh(self, name):
        for widget in self.winfo_children():
            widget.destroy()
        self.name_variable = ttk.StringVar()
        self.executable_variable = ttk.StringVar()
        self.separator_start_variable = ttk.StringVar()
        self.separator_end_variable = ttk.StringVar()
        row = 0
        self.title = ttk.Label(self)
        self.title["text"] = "SONG TRACKER"
        self.title["font"] = "Helvetica", 16
        self.title.grid(column=0, columnspan=12, row=row)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Name:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.name_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Executable:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.executable_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Separator Start:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.separator_start_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Separator End:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.separator_end_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.save_button = ttk.Button(self)
        self.save_button["text"] = "SAVE"
        self.save_button["command"] = lambda: self.save()
        self.save_button.grid(column=9, columnspan=1, row=row)
        self.delete_button = ttk.Button(self)
        self.delete_button["text"] = "DELETE"
        self.delete_button["command"] = lambda: self.delete()
        self.delete_button.grid(column=10, columnspan=1, row=row)
        self.cancel_button = ttk.Button(self)
        self.cancel_button["text"] = "CANCEL"
        self.cancel_button["command"] = lambda: self.cancel()
        self.cancel_button.grid(column=11, columnspan=1, row=row)
        song_trackers = self.manager.get_state()[self.manager.SONG_TRACKERS]
        if name in song_trackers:
            song_tracker = song_trackers[name]
            self.name_variable.set(name)
            self.executable_variable.set(song_tracker[self.manager.EXECUTABLE])
            self.separator_start_variable.set(song_tracker[self.manager.SEPARATOR_START])
            self.separator_end_variable.set(song_tracker[self.manager.SEPARATOR_END])

    def save(self):
        song_tracker = {
            self.manager.EXECUTABLE: self.executable_variable.get(),
            self.manager.SEPARATOR_START: self.separator_start_variable.get(),
            self.manager.SEPARATOR_END: self.separator_end_variable.get(),
            self.manager.SONG: ""
        }
        state = self.manager.get_state()
        state[self.manager.SONG_TRACKERS][self.name_variable.get()] = song_tracker
        self.manager.set_sate(state)
        helper.navigate_to_menu_view(self.window.menu)

    def delete(self):
        song_trackers = self.manager.get_state()[self.manager.SONG_TRACKERS]
        if self.name_variable.get() in song_trackers:
            state = self.manager.get_state()
            state[self.manager.SONG_TRACKERS].pop(self.name_variable.get())
            self.manager.set_sate(state)
        helper.navigate_to_menu_view(self.window.menu)

    def cancel(self):
        helper.navigate_to_menu_view(self.window.menu)


class Countdown(AbstractCRUDView):
    def __init__(self, window, manager):
        super().__init__(window, manager)

    def refresh(self, name):
        for widget in self.winfo_children():
            widget.destroy()
        self.name_variable = ttk.StringVar()
        self.hours_variable = ttk.IntVar()
        self.minutes_variable = ttk.IntVar()
        self.seconds_variable = ttk.IntVar()
        row = 0
        self.title = ttk.Label(self)
        self.title["text"] = "COUNTDOWN"
        self.title["font"] = "Helvetica", 16
        self.title.grid(column=0, columnspan=12, row=row)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Name:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.name_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Hours:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.hours_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Minutes:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.minutes_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Seconds:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.seconds_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.save_button = ttk.Button(self)
        self.save_button["text"] = "SAVE"
        self.save_button["command"] = lambda: self.save()
        self.save_button.grid(column=9, columnspan=1, row=row)
        self.delete_button = ttk.Button(self)
        self.delete_button["text"] = "DELETE"
        self.delete_button["command"] = lambda: self.delete()
        self.delete_button.grid(column=10, columnspan=1, row=row)
        self.cancel_button = ttk.Button(self)
        self.cancel_button["text"] = "CANCEL"
        self.cancel_button["command"] = lambda: self.cancel()
        self.cancel_button.grid(column=11, columnspan=1, row=row)
        countdowns = self.manager.get_state()[self.manager.COUNTDOWNS]
        if name in countdowns:
            countdown = countdowns[name]
            self.name_variable.set(name)
            hours = countdown[self.manager.TIME] // 3600
            minutes = (countdown[self.manager.TIME] - hours * 3600) // 60
            seconds = countdown[self.manager.TIME] - hours * 3600 - minutes * 60
            self.hours_variable.set(hours)
            self.minutes_variable.set(minutes)
            self.seconds_variable.set(seconds)

    def save(self):
        hours = 0
        try:
            hours = int(self.hours_variable.get())
        except:
            pass
        minutes = 0
        try:
            minutes = int(self.minutes_variable.get())
        except:
            pass
        seconds = 0
        try:
            seconds = int(self.seconds_variable.get())
        except:
            pass
        countdown = {
            self.manager.TIME: hours * 3600 + minutes * 60 + seconds
        }
        state = self.manager.get_state()
        state[self.manager.COUNTDOWNS][self.name_variable.get()] = countdown
        self.manager.set_sate(state)
        helper.navigate_to_menu_view(self.window.menu)

    def delete(self):
        countdowns = self.manager.get_state()[self.manager.COUNTDOWNS]
        if self.name_variable.get() in countdowns:
            state = self.manager.get_state()
            state[self.manager.COUNTDOWNS].pop(self.name_variable.get())
            self.manager.set_sate(state)
        helper.navigate_to_menu_view(self.window.menu)

    def cancel(self):
        helper.navigate_to_menu_view(self.window.menu)


class Disclaimer(AbstractCRUDView):
    def __init__(self, window, manager):
        super().__init__(window, manager)

    def refresh(self, name):
        for widget in self.winfo_children():
            widget.destroy()
        self.name_variable = ttk.StringVar()
        self.text_variable = ttk.StringVar()
        row = 0
        self.title = ttk.Label(self)
        self.title["text"] = "DISCLAIMER"
        self.title["font"] = "Helvetica", 16
        self.title.grid(column=0, columnspan=12, row=row)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Name:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.name_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.name_label = ttk.Label(self)
        self.name_label["text"] = "Text:"
        self.name_label["font"] = "Helvetica", 14
        self.name_label.grid(column=0, columnspan=2, row=row, sticky=ttk.NSEW)
        self.name_input = ttk.Entry(self)
        self.name_input["textvariable"] = self.text_variable
        self.name_input["font"] = "Helvetica", 14
        self.name_input.grid(column=3, columnspan=10, row=row, sticky=ttk.NSEW)
        row += 1
        helper.separator(self, row)
        row += 1
        self.save_button = ttk.Button(self)
        self.save_button["text"] = "SAVE"
        self.save_button["command"] = lambda: self.save()
        self.save_button.grid(column=9, columnspan=1, row=row)
        self.delete_button = ttk.Button(self)
        self.delete_button["text"] = "DELETE"
        self.delete_button["command"] = lambda: self.delete()
        self.delete_button.grid(column=10, columnspan=1, row=row)
        self.cancel_button = ttk.Button(self)
        self.cancel_button["text"] = "CANCEL"
        self.cancel_button["command"] = lambda: self.cancel()
        self.cancel_button.grid(column=11, columnspan=1, row=row)
        disclaimers = self.manager.get_state()[self.manager.DISCLAIMERS]
        if name in disclaimers:
            disclaimer = disclaimers[name]
            self.name_variable.set(name)
            self.text_variable.set(disclaimer[self.manager.TEXT])

    def save(self):
        disclaimer = {
            self.manager.TEXT: self.text_variable.get(),
        }
        state = self.manager.get_state()
        state[self.manager.DISCLAIMERS][self.name_variable.get()] = disclaimer
        self.manager.set_sate(state)
        helper.navigate_to_menu_view(self.window.menu)

    def delete(self):
        disclaimers = self.manager.get_state()[self.manager.DISCLAIMERS]
        if self.name_variable.get() in disclaimers:
            state = self.manager.get_state()
            state[self.manager.DISCLAIMERS].pop(self.name_variable.get())
            self.manager.set_sate(state)
        helper.navigate_to_menu_view(self.window.menu)

    def cancel(self):
        helper.navigate_to_menu_view(self.window.menu)
