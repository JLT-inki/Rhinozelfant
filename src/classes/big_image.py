"""File containing the BigImage class."""

# Import for the create_image_from_file method
from __future__ import annotations

# Import used Python libraries
import PIL.Image
import numpy as np

# Import the used Pixel class
from classes.pixel import Pixel

class BigImage:
    """
    Class representing one image.

    Attributes
    ----------
    pixels: list[list[Pixel]]
        The pixels of the image.

    Methods
    -------
    set_pixels
        Set the pixels of the image.
    get_pixels
        Return the pixels of the image.
    create_image_from_file
        Create one BigImage object from a PNG file.

    Notes
    -----
    The class is called BigImage and not just Image since the Image keyword is
    already used by the Pillow package.

    """

    def __init__(self, pixels: list[list[Pixel]]) -> None:
        """
        Create one BigImage object with the given parameters.

        Parameters
        ----------
        pixels: list[list[Pixel]]
            The pixels of the image.

        """
        self.set_pixels(pixels)

    def set_pixels(self, pixels: list[list[Pixel]]) -> None:
        """
        Set the pixels of the image.

        Parameters
        ----------
        pixels: list[list[Pixel]]
            The pixels of the image.

        """
        self.pixels: list[list[Pixel]] = pixels

    def get_pixels(self) -> list[list[Pixel]]:
        """
        Return the pixels of the image.

        Returns
        -------
        pixels: list[list[Pixel]]
            The pixels of the image.

        """
        return self.pixels

    def get_pixel_at(self, row: int, column: int) -> Pixel:
        """
        Return a specific pixel of the image.

        Parameters
        ----------
        row: int
            Row of the image in which the pixel is.
        column: int
            Column of the image in which the pixel is.

        Returns
        -------
        Pixel
            Pixel at the specified position.

        """
        return self.get_pixels()[row][column]

    @staticmethod
    def create_image_from_file(path_to_file: str) -> BigImage:
        """
        Create one BigImage object from a PNG file.

        Parameters
        ----------
        path_to_file: str
            Path to the PNG file.

        Returns
        -------
        BigImage
            Newly created BigImage object.

        """
        # Read the image
        image: PIL.Image = PIL.Image.open(path_to_file)

        # Initialize the array that holds the pixels
        pixels: list[list[Pixel]] = []

        # Get the pixels value for each pixel
        for y in range(image.height):
            # Add a sublist for each row of the image
            pixels.append([])

            for x in range(image.width):
                pixels[y].append(Pixel(
                    image.getpixel((x, y))[0], image.getpixel((x, y))[1],
                    image.getpixel((x, y))[2]))

        # Return a newly created BigImage object
        return BigImage(pixels)

    def show_image(self) -> None:
        """Show an image on the screen."""
        # Array holding the RGB values of each pixel
        pixels: list[list[tuple[int, int, int]]] = []

        for count, row in enumerate(self.get_pixels()):
            # Add a new sublist for each row of the image
            pixels.append([])

            for pixel in row:
                pixels[count].append((
                    pixel.get_red_value(), pixel.get_green_value(),
                    pixel.get_blue_value()))

        # Convert the pixels into an array using numpy
        array = np.array(pixels, dtype=np.uint8)

        # Create a pillow image
        image: PIL.Image = PIL.Image.fromarray(array)

        # Show the image
        image.show()

    def find_rhinolzelfant(self) -> BigImage:
        """
        Find the Rhinolzelfant in the image and return a new image that shows it.

        Returns
        -------
        BigImage
            BigImage object in which the Rhinolzelfant is drawn into.

        """
        # Initialize the array that holds the pixels as a copy of the original image
        pixels: list[list[Pixel]] = [row.copy() for row in self.get_pixels()]

        # Get the height and width of the image
        height: int = len(self.get_pixels())
        width: int = len(self.get_pixels()[0])

        for y in range(height):
            for x in range(width):
                # Check vertically
                if (y + 1 < height and
                    Pixel.two_pixels_are_the_same(
                        self.get_pixel_at(y, x), self.get_pixel_at(y + 1, x))):
                    # Change the pixels
                    pixels[y][x] = Pixel(255, 255, 255)
                    pixels[y + 1][x] = Pixel(255, 255, 255)

                # Check horizontally
                if (x + 1 < width and
                    Pixel.two_pixels_are_the_same(
                        self.get_pixel_at(y, x), self.get_pixel_at(y, x + 1))):
                    pixels[y][x] = Pixel(255, 255, 255)
                    pixels[y][x + 1] = Pixel(255, 255, 255)

        # Return the image containing the Rhinolzelfant
        return BigImage(pixels)

    def save_image(self, file_name: str) -> None:
        """
        Save an image as a PNG file.

        Parameters
        ----------
        file_name: str
            Name under which the file should be saved.

        """
        # Array holding the RGB values of each pixel
        pixels: list[list[tuple[int, int, int]]] = []

        for count, row in enumerate(self.get_pixels()):
            # Add a new sublist for each row of the image
            pixels.append([])

            for pixel in row:
                pixels[count].append((
                    pixel.get_red_value(), pixel.get_green_value(),
                    pixel.get_blue_value()))

        # Convert the pixels into an array using numpy
        array = np.array(pixels, dtype=np.uint8)

        # Create a pillow image
        image: PIL.Image = PIL.Image.fromarray(array)

        # Save the image
        image.save(file_name)
