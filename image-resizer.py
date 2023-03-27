# Set the input and output directory paths
import os
from PIL import Image
input_directory = ""
output_directory = ""

# Loop through all the files in the input folder
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Open the image
        img = Image.open(os.path.join(input_directory, filename))

        # Resize the image
        new_size = (768, 768)#custom here
        resized_img = img.resize(new_size)

        # Save the resized image with a new filename in the output folder
        new_filename = os.path.splitext(filename)[0] + ".png"
        resized_img.save(os.path.join(output_directory, new_filename))
print('\n[1;32mDone')