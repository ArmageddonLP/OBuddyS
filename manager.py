import json
import os
import threading
import time

import helper


class Manager:
    OUTPUT_FILE_DIRECTORY = "output_files/"
    SONG_TRACKERS = "song_trackers"
    COUNTDOWNS = "countdowns"
    DISCLAIMERS = "disclaimers"
    EXECUTABLE = "executable"
    SEPARATOR_START = "separator_start"
    SEPARATOR_END = "separator_end"
    SONG = "song"
    TIME = "time"
    TEXT = "text"
    thread = None
    lock = threading.Lock()
    state = {
        SONG_TRACKERS: {
            "youtube": {
                EXECUTABLE: "YouTube Music Desktop App.exe",
                SEPARATOR_START: "  | ",
                SEPARATOR_END: " |  ",
                SONG: ""
            },
            "spotify": {
                EXECUTABLE: "Spotify.exe",
                SEPARATOR_START: "  | ",
                SEPARATOR_END: " |  ",
                SONG: ""
            }
        },
        COUNTDOWNS: {
            "countdown": {
                TIME: 0
            }
        },
        DISCLAIMERS: {
            "disclaimer": {
                TEXT: ""
            }
        }
    }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Manager, cls).__new__(cls)
            cls.state = cls.instance.get_state()
            cls.instance.start_thread()
        return cls.instance

    def start_thread(self):
        self.thread = threading.Thread(target=self.thread_cycle, args=(), daemon=True)
        self.thread.start()

    def thread_cycle(self):
        time.sleep(1)
        while 1:
            start = time.time()
            log = ""
            for song_tracker in self.state[self.SONG_TRACKERS].items():
                name = song_tracker[0]
                executable = song_tracker[1][self.EXECUTABLE]
                separator_start = song_tracker[1][self.SEPARATOR_START]
                separator_end = song_tracker[1][self.SEPARATOR_END]
                song = helper.current_song(executable)
                self.state[self.SONG_TRACKERS][name][self.SONG] = song
                text = separator_start + song + separator_end
                self.__output_file__(name, text)
                log += "'name':'" + song_tracker[0] + "', "
                log += "'" + self.EXECUTABLE + "':'" + song_tracker[1][self.EXECUTABLE] + "', "
                log += "'" + self.SEPARATOR_START + "':'" + song_tracker[1][self.SEPARATOR_START] + "', "
                log += "'" + self.SEPARATOR_END + "':'" + song_tracker[1][self.SEPARATOR_END] + "', "
                log += "'" + self.SONG + "':'" + song_tracker[1][self.SONG] + "'\n"
            for countdown in self.state[self.COUNTDOWNS].items():
                name = countdown[0]
                t = countdown[1][self.TIME]
                if t > 0: t -= 1
                self.state[self.COUNTDOWNS][name][self.TIME] = t
                text = helper.time_to_string(t)
                self.__output_file__(name, text)
                log += "'name':'" + countdown[0] + "', "
                log += "'" + self.TIME + "':'" + str(countdown[1][self.TIME]) + "'\n"
            for disclaimer in self.state[self.DISCLAIMERS].items():
                name = disclaimer[0]
                text = disclaimer[1][self.TEXT]
                self.__output_file__(name, text)
                log += "'name':'" + disclaimer[0] + "', "
                log += "'" + self.TEXT + "':'" + disclaimer[1][self.TEXT] + "'\n"
            print(log)
            self.set_sate(self.state)
            end = time.time()
            time.sleep(1 - end + start)

    def __output_file__(self, name, text):
        os.makedirs(os.path.dirname(self.OUTPUT_FILE_DIRECTORY), exist_ok=True)
        with open(self.OUTPUT_FILE_DIRECTORY + name + ".txt", "w") as outfile:
            outfile.write(text)

    def get_state(self):
        try:
            with open("state.json", "r") as infile:
                self.state = json.load(infile)
        except FileNotFoundError:
            self.set_sate(self.state)
        except json.decoder.JSONDecodeError:
            self.set_sate(self.state)
        return self.state

    def set_sate(self, state):
        self.lock.acquire()
        self.state = state
        with open("state.json", "w") as outfile:
            json.dump(self.state, outfile)
        self.lock.release()
