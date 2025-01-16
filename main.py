from tkinter import Tk,filedialog
from PIL import Image
def get_path():
    root=Tk()
    root.withdraw()
    path=filedialog.askopenfilename(
        title='Select an image file',
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    return path
def save_image_file():
    root = Tk()
    root.withdraw()  
    
    save_path = filedialog.asksaveasfilename(
        title="Save Resized Image",
        defaultextension=".jpg",  
        filetypes=[("JPEG", "*.jpg;*.jpeg"), ("PNG", "*.png"), ("All Files", "*.*")]
    )
    
    return save_path
def resize():
    img_path=get_path()
    if img_path:
        img=Image.open(img_path)
        new_width=int(input("Enter the new width of the image: "))
        new_height=int(input("Enter the new height of the image: "))
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        save_path = save_image_file()

        if save_path:  
            resized_img.save(save_path)
            print(f"Resized image saved as '{save_path}'")

            
            resized_img.show()
        else:
            print("No save location selected.")
    else:
        print("No file selected.")


resize()