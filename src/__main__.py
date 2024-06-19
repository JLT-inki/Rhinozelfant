"""Main file of the project 'Rhinozelfant'."""

# Import used Python libraries
import sys

# Import used classes
from classes.big_image import BigImage

# Constants used for reading/saving the images
FILE_BEGINNING: str = "rhinozelfant"
FILE_ENDING: str = ".png"
INPUT_PATH: str = "./../input/"
OUTPUT_PATH: str = "./../output/"

def main() -> int:
    """Check if there is a Rhinolzelfant hidden in each image and shot it."""
    # Go through each input image, find the Rhinolzelfant and save a copy with it
    for i in range(1, 10):
        # Print the current image
        print("Current image:", FILE_BEGINNING + str(i))

        # Create the image
        big_image: BigImage = BigImage.create_image_from_file(
            INPUT_PATH + FILE_BEGINNING + str(i) + FILE_ENDING)
        print("\tFile successfully read!")

        # Find the Rhinolzelfant
        image_with_rhinolzelfant: BigImage = big_image.find_rhinolzelfant()
        print("\tChecked for Rhinolzelfant!")

        # Save the image
        image_with_rhinolzelfant.save_image(
            OUTPUT_PATH + FILE_BEGINNING + str(i) + FILE_ENDING)
        print("\tSaved the image.")

    # Return exitcode 0 indicating success
    return 0


if __name__ == "__main__":
    sys.exit(main())
