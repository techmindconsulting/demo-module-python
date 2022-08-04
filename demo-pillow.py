import os, sys


import PIL.Image as Image

size = (128, 128)


for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail.jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)