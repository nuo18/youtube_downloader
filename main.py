from pytube import YouTube
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x550")
        
        #Title
        self.label = customtkinter.CTkLabel(self, font=("Helvetica", 50),text="Youtube downloader", fg_color="transparent")
        self.label.pack(padx=20, pady=40)

        #User enters link here
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Youtube link here", width=500)
        self.entry.pack(padx=20, pady=20)

        #Download button
        self.button = customtkinter.CTkButton(self, text="Download mp3", command=self.download)
        self.button.grid(row=1, column=0, padx=20, pady=(0, 20))
        self.button1 = customtkinter.CTkButton(self, text="Download mp4", command=self.download)
        self.button1.grid(row=1, column=0, padx=20, pady=(0, 20))

        #Progress bar, changes according to value in set
        self.progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal", height=20, width=400)
        self.progressbar.set(0.5)
        self.progressbar.pack(padx=20, pady=20)

    def download(self):
        #Youtube object
        self.link = self.entry.get()
        self.yt = YouTube(self.link)

        #Showing title and size of the video
        self.label2 = customtkinter.CTkLabel(self, text=self.yt.title, fg_color="transparent")
        self.label2.pack(padx=20, pady=20)

        #Downloads video
        self.video = self.yt.streams.get_highest_resolution()
        self.video.download()

        #Done Icon
        self.label3 = customtkinter.CTkLabel(self,text="Done!", fg_color="transparent")
        self.label3.pack(padx=20, pady=20)

app = App()
app.mainloop()