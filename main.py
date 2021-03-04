from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    arrayException = ["Music", "Video", "Archive", "Image", "PDF", "Text", "Table"]

    allExtension = [
        ["mid", "rmi", "mus", "wav", "ra", "ram", "rm", "rmm", "mp3", "m3u", "aif", "aiff", "aifc", "snd", "au"],
        # Музыкальные файлы
        ["mov", "mpeg4", "mp4", "avi", "wmv", "mpegps", "flv", "3gp", "webm", "dnxhr", "prores", "cineform"],
        # Видео типы файлов
        ["arj", "zip", "rar", "z", "tar", "cab"],  # Архивные типы файлов
        ["bmp", "gif", "jpg", "jpeg", "tif", "tiff", "dcx", "qfx", "pcx", "dib", "png", "rle", "tga", "psd", "iff"],
        # Графические растровые типы файлов
        ["pdf"],  # Pdf тип файла
        ["doc", "docx", "dot", "dotx", "", "", "txt", "rtf"],  # Текстовые типы файлов
        ["csv", "ods"]]  # Табличные типы файлов

    def checkExtension(self, folder_dest, extension=" "):
        for i in range(len(self.allExtension)):
            for j in range(len(self.allExtension[i])):
                if self.allExtension[i][j].lower() == extension[1].lower():
                    if not os.path.exists(folder_dest + "/" + str(self.arrayException[i])):
                        os.mkdir(folder_dest + "/" + str(self.arrayException[i]))
                        print("Была создана папка по пути: " + folder_dest + "/" + str(self.arrayException[i]))
                    return "/" + self.arrayException[i] + "/" + extension[0] + "." + extension[1]
        if not os.path.exists(folder_dest + "/" + extension[1]):
            os.mkdir(folder_dest + "/" + extension[1])
            print("Была создана папка по пути: " + folder_dest + "/" + extension[1])
            return "/" + extension[1] + "/" + extension[0] + "." + extension[1]
        else:
            return "None"

    def sortingFile(self):
        print()
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            # file=os.getcwdb()+"\\"+filename
            # new_path= self.checkExtension(extension[1])
            file = folder_track + "/" + filename
            if extension[0] != "" and (extension.__len__() > 1):
                result = self.checkExtension(folder_dest, extension)
                if result != "None":
                    new_path = folder_dest + result
                    print("Файл был перемещён в: " + new_path)
                    os.rename(file, new_path)

    def on_modified(self, event):
        self.sortingFile()


folder_track = os.path.dirname(os.path.abspath(__file__))
folder_dest = os.path.dirname(os.path.abspath(__file__))

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while (True):
        handle.sortingFile()
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    print("Произошла ошибка :(")
