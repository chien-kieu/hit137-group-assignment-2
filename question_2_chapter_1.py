import time
from PIL import Image

# Load the original image
original_image_path = 'chapter1.jpg'
original_image = Image.open(original_image_path)

# Get the size of the image
width, height = original_image.size

# Generate a number (n)
current_time = int(time.time())
generated_number = (current_time % 100) + 50

# If the generated number is even, add 10 to it
if generated_number % 2 == 0:
    generated_number += 10

# Create a new image with the modified pixel values
new_image = Image.new('RGB', (width, height))

for y in range(height):
    for x in range(width):
        # Get the original pixel values (r, g, b)
        original_pixel = original_image.getpixel((x, y))

        # Modify the pixel values by adding the generated number
        modified_pixel = (
            original_pixel[0] + generated_number,
            original_pixel[1] + generated_number,
            original_pixel[2] + generated_number
        )

        # Set the modified pixel values in the new image
        new_image.putpixel((x, y), modified_pixel)

# Save the new image
new_image_path = 'chapter1out.png'
new_image.save(new_image_path)

# Calculate the sum of red (r) pixel values in the new image
red_pixel_sum = sum([pixel[0] for pixel in new_image.getdata()])

# Print the sum of red pixel values
print("Sum of Red (r) Pixel Values in the New Image:", red_pixel_sum)

