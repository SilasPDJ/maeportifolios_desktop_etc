from defs_utils import list_dir
from PIL import Image

images = list_dir(r'C:\Users\Silas\Desktop\projeto-mae\MATERIAS_CRIA_FILES\Geografia e Ciências\DAVI_SILVA_DUARTE',
                  True, endswith='.jpg')

"""
#Read the two images
image1 = Image.open(images[0])
image1.show()
image2 = Image.open(images[1])
image2.show()
"""


def create_images(*imgs):

    for img in imgs:
        # print(img)
        image = Image.open(img)
        yield image


def xy_size(im):
    yield im.size


my_ims = create_images(*images)
ims_list = list(my_ims)
print(ims_list)
tam = len(list(my_ims))

_s1ze = ims_list[0].size

new_image = Image.new('RGB', (5*_s1ze[0], 5*_s1ze[1]),
                      (250, 250, 250))

new_image.paste(ims_list[0], (0, 0))
# é o lugar onde colo...
new_image.paste(ims_list[2], (1200, 5))

new_image.save("merged_image-p2.jpg","JPEG", quality=100)
new_image.show()