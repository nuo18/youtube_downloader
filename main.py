from pytube import YouTube
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        #Centre the grid
        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        #Title
        self.label = customtkinter.CTkLabel(self, font=("Helvetica", 50), text="Youtube Downloader", fg_color="transparent")
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        
        #User enters link here
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Youtube link here", width=300)
        self.entry.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        
        #Download button
        self.button = customtkinter.CTkButton(self, text="Download mp3", command=self.download)
        self.button.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.button1 = customtkinter.CTkButton(self, text="Download mp4", command=self.download)
        self.button1.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        
        #Progress bar, changes according to value in set
        self.progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal", width=200, height=20)
        self.progressbar.set(0.3)
        self.progressbar.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    def download_mp3(self):
        #Youtube object
        self.link = self.entry.get()
        self.yt = YouTube(self.link)

        #Showing title and size of the video
        self.label2 = customtkinter.CTkLabel(self, text=self.yt.title, fg_color="transparent")
        self.label2.grid(row=4, column=0, padx=20, pady=20)

        #Downloads video
        self.video = self.yt.streams.get_highest_resolution()
        self.video.download()

        #Done Icon
        self.label3 = customtkinter.CTkLabel(self,text="Done!", fg_color="transparent")
        self.label3.grid(row=5, column=0, padx=20, pady=20)
    
    def download_mp4(self):
        #Youtube object
        self.link = self.entry.get()
        self.yt = YouTube(self.link)

        #Showing title and size of the video
        self.label2 = customtkinter.CTkLabel(self, text=self.yt.title, fg_color="transparent")
        self.label2.grid(row=4, column=0, padx=20, pady=20)

        #Downloads video
        self.video = self.yt.streams.get_highest_resolution()
        self.video.download()

        #Done Icon
        self.label3 = customtkinter.CTkLabel(self,text="Done!", fg_color="transparent")
        self.label3.grid(row=5, column=0, padx=20, pady=20)

app = App()
app.mainloop()