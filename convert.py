from PIL import Image
import os
import argparse


def img_downscale(filepath):
    img_info = get_num_pixels(filepath)
    if img_info:
        if img_info[1] >=2500000:
            if img_info[2]:
                basewidth = 900
                wpercent = (basewidth/float(img_info[0].size[1]))
                hsize = int((float(img_info[0].size[0])*float(wpercent)))
            else:
                basewidth = 1440
                wpercent = (basewidth/float(img_info[0].size[0]))
                hsize = int((float(img_info[0].size[1])*float(wpercent)))
            img = img_info[0].resize((basewidth,hsize), Image.ANTIALIAS)
            img.save(filepath)

def get_num_pixels(filepath):
    try:
        img = Image.open(filepath)
        width, height = img.size
        if height >= width:
            portrait = True
        else:
            portrait = False
        return img, width*height, portrait
    except Exception as e:
        print("### Can not open: " + str(filepath) + "\n It is't an image file. ###\n")
        return None

def main(folder):
    print("Downscale images...")
    for filename in os.listdir(folder):
        print(folder + filename)
        img_downscale(folder + filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', action='store', required = True, dest='folder', help='Images folder path')
    args = parser.parse_args()
    folder_path = args.folder
    main(folder_path)
