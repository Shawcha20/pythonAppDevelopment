from tkinter import Tk, filedialog, Button, Label
from PIL import Image, ImageTk, ImageFilter

currentImage = None  # Define global image

def main():
    global currentImage, imageLabel

    window = Tk()
    window.title("Photo Filter App")
    window.geometry("800x600")

    def loadImage():
        
        filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if filePath:
            img = Image.open(filePath)
            displayImage(img)

    def applyFilter(filterType):
        global currentImage
        if currentImage:
            if filterType == 'grayscale':
                filteredImg = currentImage.convert("L")
            elif filterType == "blur":
                filteredImg = currentImage.filter(ImageFilter.BLUR)
            elif filterType == "sharpen":
                filteredImg = currentImage.filter(ImageFilter.SHARPEN)
            else:
                return
            displayImage(filteredImg)

    def displayImage(img):
        global currentImage
        currentImage = img
        tkImage = ImageTk.PhotoImage(img.resize((400, 400)))
        imageLabel.config(image=tkImage)
        imageLabel.image = tkImage

    # GUI Components
    loadButton = Button(window, text="Load Image", command=loadImage)
    loadButton.pack(pady=10)

    imageLabel = Label(window)
    imageLabel.pack(pady=10)

    grayscaleButton = Button(window, text="Grayscale", command=lambda: applyFilter("grayscale"))
    grayscaleButton.pack(pady=10)

    blurButton = Button(window, text="Blur", command=lambda: applyFilter("blur"))
    blurButton.pack(pady=10)

    sharpenButton = Button(window, text="Sharpen", command=lambda: applyFilter("sharpen"))
    sharpenButton.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
