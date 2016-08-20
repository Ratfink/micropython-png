# micropython-png

A derivative of [PyPNG](https://github.com/drj11/pypng) for use with
[MicroPython](https://github.com/micropython/micropython).

Quite a few features of PyPNG have been removed to allow the module to work
better in constrained systems.  Support for ancillary chunks has been removed.
Several API functions from PyPNG's Reader class have been removed as well, such
as the floating-point image conversion function.

It is recommended to use mpy-cross to pre-compile this module, especially for
use on microcontrollers.  On some systems, such as the ESP8266, this may mean
compiling it as a frozen module.  Do not forget that itertools is required by
micropython-png.
