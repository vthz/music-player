# this is main python file for music player
# Developed by Shaheen Naiyer 12072021 @ 2204hrs
from tkinter import *
import os

import pygame
from pygame import mixer
from PIL import Image

music_folder = "D:\Shaheen DEC2020 v7.0\My Music"
music_list = []
for i in os.listdir(music_folder):
    music_list.append(i)
size = len(music_list)
image_file_path = "music_pic.png"


class MusicPlayer:
    def __init__(self, window):
        window.geometry('670x320')
        window.title("Music Player")
        window.resizable(0, 0)
        window.config(bg='grey')

        Update = Button(window, text="Update", width=30, height=1, command=self.update)
        Play = Button(window, text='Play', width=30, height=1, command=self.play)
        Pause = Button(window, text='Pause', width=30, height=1, command=self.pause)
        Stop = Button(window, text='Stop', width=30, height=1, command=self.stop)

        self.new_music_folder = StringVar(window)
        self.Path = Entry(window, width=50, textvariable=self.new_music_folder)
        self.Path.insert(0, music_folder)
        self.Player_label = Label(window, text="No song is being played", height=2, width=30, bg="white", borderwidth=4,
                                  relief='groove')
        self.Song_list = Listbox(window, bg='white', height=10, width=36, fg="black")
        self.img = PhotoImage(file=image_file_path)
        self.img = self.img.subsample(4, 4)
        self.Image_label = Label(window, image=self.img, width=210, borderwidth=4, relief='groove')

        self.Path.grid(row=0, column=2, sticky=W, pady=2, padx=2)
        self.Song_list.grid(row=1, column=2, sticky=W, pady=2, padx=2)
        self.Player_label.grid(row=2, column=1, sticky=W, pady=2, padx=2)
        self.Image_label.grid(row=1, column=1, sticky=W, pady=2, padx=2)
        Update.grid(row=3, column=0, sticky=W, pady=2, padx=2)
        Play.grid(row=3, column=1, sticky=W, pady=2, padx=2)
        Pause.grid(row=3, column=2, sticky=W, pady=2, padx=2)
        Stop.grid(row=4, column=1, sticky=W, pady=2, padx=2)

        self.music_file = False
        self.playing_state = False

    def update(self):
        self.Song_list.delete(0, 'end')
        global music_folder
        music_folder = self.new_music_folder.get()
        self.Player_label.config(text="Location updated to " + str(music_folder))
        music_list = []
        for i in os.listdir(music_folder):
            if i.endswith(".mp3"):
                music_list.append(i)
        global size
        size = len(music_list)
        for i in range(size):
            self.Song_list.insert(i + 1, str(music_list[i]))

    def play(self):
        self.Path.delete(0, 'end')
        current_song = ""
        for i in self.Song_list.curselection():
            current_song = self.Song_list.get(i)
        self.Path.insert(0, music_folder)
        self.music_file = music_folder + "\\" + current_song

        if self.music_file:
            pygame.init()
            # mixer.init()
            try:
                mixer.music.load(self.music_file)
                self.Player_label.config(text=str(current_song))
                mixer.music.play()
            except:
                self.Player_label.config(text="Can not play the song!")
        else:
            self.Player_label.config(text="Song Cant be played!")

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()


root = Tk()
app = MusicPlayer(root)
root.mainloop()
