from pytube import YouTube
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x550")
        
        self.label = customtkinter.CTkLabel(self, font=("Helvetica", 50),text="Youtube downloader", fg_color="transparent")
        self.label.pack(padx=20, pady=40)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Youtube link here", width=500)
        self.entry.pack(padx=20, pady=20)

        self.button = customtkinter.CTkButton(self, text="Download", command=self.download)
        self.button.pack(padx=20, pady=20)

    def download(self):
        self.link = self.entry.get()
        self.yt = YouTube(self.link)

        self.video = self.yt.streams.get_highest_resolution()
        self.video.download()

        self.label2 = customtkinter.CTkLabel(self,text="Done!", fg_color="transparent")
        self.label2.pack(padx=20, pady=20)

app = App()
app.mainloop()