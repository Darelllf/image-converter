import os
from PIL import Image
folder_path = '' 
output_folder_path = '' 
format_image = '.png' #@param {type:"string"} [".jpg", ".png",".jpeg", ".pdf"]  
output_image_format = '.jpeg'   #@param {type:"string"} [".jpg", ".png",".jpeg", ".pdf"]  
for filename in os.listdir(folder_path):
    if filename.endswith(format_image):
        with Image.open(os.path.join(folder_path, filename)) as png_image:
            rgb_image = png_image.convert('RGB')
            jpg_filename = os.path.splitext(filename)[0] + (output_image_format)
            jpg_filepath = os.path.join(output_folder_path, jpg_filename)
            rgb_image.save(jpg_filepath)

print('Done')
