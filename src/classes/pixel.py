"""File containing the pixel class."""

# Import for the two_pixels_are_the_same method
from __future__ import annotations

class Pixel:
    """
    Class representing one pixel.

    Attributes
    ----------
    red_value: int
        Red value of the pixel.
    green_value: int
        Green value of the pixel.
    blue_value: int
        Blue value of the pixel.

    Methods
    -------
    set_red_value
        Set the red value of the pixel.
    set_green_value
        Set the green value of the pixel.
    set_blue_value
        Set the blue value of the pixel.
    get_red_value
        Return the red value of the pixel.
    get_green_value
        Return the green value of the pixel.
    get_blue_value
        Return the blue value of the pixel.
    two_pixels_are_the_same
        Compare two pixels and check whether they are the same.

    """

    def __init__(self, red_value: int, green_value: int, blue_value: int) -> None:
        """
        Create a Pixel object with the given parameters.

        Parameters
        ----------
        red_value: int
            Red value of the pixel.
        green_value: int
            Green value of the pixel.
        blue_value: int
            Blue value of the pixel.

        """
        self.set_red_value(red_value)
        self.set_green_value(green_value)
        self.set_blue_value(blue_value)

    def set_red_value(self, red_value: int) -> None:
        """
        Set the red value of the pixel.

        Parameters
        ----------
        red_value: int
            Red value of the pixel.

        """
        self.red_value: int = red_value

    def set_green_value(self, green_value: int) -> None:
        """
        Set the green value of the pixel.

        Parameters
        ----------
        green_value: int
            Red value of the pixel.

        """
        self.green_value: int = green_value

    def set_blue_value(self, blue_value: int) -> None:
        """
        Set the blue value of the pixel.

        Parameters
        ----------
        blue_value: int
            Red value of the pixel.

        """
        self.blue_value: int = blue_value

    def get_red_value(self) -> int:
        """
        Return the red value of the pixel.

        Returns
        -------
        red_value: int
            Red value of the pixel.

        """
        return self.red_value

    def get_green_value(self) -> int:
        """
        Return the green value of the pixel.

        Returns
        -------
        green_value: int
            Green value of the pixel.

        """
        return self.green_value

    def get_blue_value(self) -> int:
        """
        Return the blue value of the pixel.

        Returns
        -------
        blue_value: int
            Blue value of the pixel.

        """
        return self.blue_value

    @staticmethod
    def two_pixels_are_the_same(pixel1: Pixel, pixel2: Pixel) -> bool:
        """
        Compare two pixels and check whether they are the same.

        Parameters
        ----------
        pixel1: Pixel
            First pixel of the comparison.
        pixel2: Pixel
            Second pixel of the comparison.

        Returns
        -------
        bool
            TRUE if the RGB values of the two pixels match, otherwise FALSE.

        """
        return (pixel1.get_red_value() == pixel2.get_red_value() and
                pixel1.get_green_value() == pixel2.get_green_value() and
                pixel1.get_blue_value() == pixel2.get_blue_value())
