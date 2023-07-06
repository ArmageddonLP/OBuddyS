import ttkbootstrap as ttk
import os
import win32con
import win32api
import win32gui
import win32process


def time_to_string(t):
    h = (t // 3600)
    m = (t - (h * 3600)) // 60
    s = (t - (h * 3600) - (m * 60))
    return str(h).rjust(2, '0') + "h" + str(m).rjust(2, '0') + "m" + str(s).rjust(2, '0') + "s"


def enumWindowsToTitlesByPid(window, param):
    pid = param.get("pid", None)
    titles = param.get("titles", None)
    if win32process.GetWindowThreadProcessId(window)[1] == pid:
        title = win32gui.GetWindowText(window)
        titles.append(title)

def titlesByPid(pid):
    titles = []
    param = {
        "pid": pid,
        "titles": titles,
    }
    win32gui.EnumWindows(enumWindowsToTitlesByPid, param)
    return titles


def pidsByExecutable(executable):
    pids = []
    for pid in win32process.EnumProcesses():
        try:
            process = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, 0, pid)
        except:
            continue
        try:
            ex = win32process.GetModuleFileNameEx(process, None).split(os.path.sep)[-1]
        except:
            win32api.CloseHandle(process)
            continue
        if ex.lower() == executable.lower():
            pids.append(pid)
        win32api.CloseHandle(process)
    return pids


def current_song(executable):
    pids = pidsByExecutable(executable)
    for pid in pids:
        titles = titlesByPid(pid)
        for title in titles:
            if title != "":
                return title
    return ""


def configure_columns(tk):
    tk.columnconfigure(0, weight=1)
    tk.columnconfigure(1, weight=1)
    tk.columnconfigure(2, weight=1)
    tk.columnconfigure(3, weight=1)
    tk.columnconfigure(4, weight=1)
    tk.columnconfigure(5, weight=1)
    tk.columnconfigure(6, weight=1)
    tk.columnconfigure(7, weight=1)
    tk.columnconfigure(8, weight=1)
    tk.columnconfigure(9, weight=1)
    tk.columnconfigure(10, weight=1)
    tk.columnconfigure(11, weight=1)


def navigate_to_menu_view(view):
    view.refresh()
    view.tkraise()


def navigate_to_crud_view(view, name):
    view.refresh(name)
    view.tkraise()


def separator(view, row):
    ttk.Separator(view).grid(column=0, columnspan=12, row=row, sticky=ttk.NSEW, pady=5)
