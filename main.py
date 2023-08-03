from pytube import YouTube
import customtkinter
import threading
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x550")
        
        #Title
        self.label = customtkinter.CTkLabel(self, font=("Helvetica", 50), text="Youtube downloader", fg_color="transparent")
        self.label.pack(padx=20, pady=40)

        #User enters link here
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Youtube link here", width=500)
        self.entry.pack(padx=20, pady=20)

        #Download buttons
        self.button_mp3 = customtkinter.CTkButton(self, text="Download mp3", command=self.download_audio)
        self.button_mp3.pack(padx=20, pady=(0, 20))

        self.button_mp4 = customtkinter.CTkButton(self, text="Download mp4", command=self.download_video)
        self.button_mp4.pack(padx=20, pady=(0, 20))

        #Bytes downloaded label
        self.bytes_label = customtkinter.CTkLabel(self, text="", fg_color="transparent")
        self.bytes_label.pack(padx=20, pady=20)

    def download_audio(self):
        self.download("audio")

    def download_video(self):
        self.download("video")

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        self.bytes_label.config(text=f"{bytes_downloaded}/{total_size} bytes downloaded")

    def download(self, download_type):
        self.link = self.entry.get()
        self.yt = YouTube(self.link, on_progress_callback=self.on_progress)

        # Showing title and size of the video
        self.label2 = customtkinter.CTkLabel(self, text=self.yt.title, fg_color="transparent")
        self.label2.pack(padx=20, pady=20)

        try:
            if download_type == "audio":
                # Downloads audio if available
                self.audio = self.yt.streams.filter(only_audio=True).first()
                if self.audio:
                    self.audio.download()
                else:
                    raise Exception("No audio stream available for this video.")
            elif download_type == "video":
                # Downloads video
                self.video = self.yt.streams.get_highest_resolution()
                self.video.download()

            # Done Icon
            self.label3 = customtkinter.CTkLabel(self, text="Done!", fg_color="transparent")
            self.label3.pack(padx=20, pady=20)

        except Exception as e:
            # Error message
            self.label3 = customtkinter.CTkLabel(self, text=f"Error: {str(e)}", fg_color="red")
            self.label3.pack(padx=20, pady=20)

app = App()
app.mainloop()
