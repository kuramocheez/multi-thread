import time
import concurrent.futures
from PIL import Image

image_array = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg',
    '7.jpg',
    '8.jpg',
    '9.jpg',
    '10.jpg',
    '11.jpg',
    '12.jpg',
    '13.jpg',
    '14.jpg',
    '15.jpg',
    '16.jpg',
    '17.jpg',
    '18.jpg',
    '19.jpg',
    '20.jpg',
    '21.jpg',
    '22.jpg',
    '23.jpg',
    '24.jpg',
    '25.jpg',
    '26.jpg',
    '27.jpg',
    '28.jpg',
    '29.jpg',
    '30.jpg',
    '31.jpg',
    '32.jpg',
    '33.jpg',
    '34.jpg',
    '35.jpg',
    '36.jpg',
    '37.jpg',
    '38.jpg',
    '39.jpg',
    '40.jpg',
    '41.jpg',
    '42.jpg',
    '43.jpg',
    '44.jpg',
    '45.jpg',
    '46.jpg',
    '47.jpg',
    '48.jpg',
    '49.jpg',
    '50.jpg'
]

total_time_start = time.perf_counter()


def resize_img(img_name):
    img = Image.open('image/'+img_name)
    new_size = (300, 400)
    split_name = img_name.split('.')
    resized_image = img.resize(new_size)
    resized_image.save(f'resize/{split_name[0]}_resize.jpg')
    print(f'{img_name} was processed to resize...\n')


def compress_image(img_name):
    img = Image.open('image/'+img_name)
    quality = 50

    split_name = img_name.split('.')

    img.save(f'compress/{split_name[0]}_compressed.jpg', optimize=True, quality=quality)
    print(f'{img_name} was processed to compress...\n')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(compress_image, image_array)
    executor.map(resize_img, image_array)


total_end_time = time.perf_counter()

print(f'Finished in {total_end_time-total_time_start} seconds')
