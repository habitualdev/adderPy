import lib.snip as snip
from PIL import ImageGrab
import lib.translate as translate
import cv2
import pytesseract
import numpy

monitor = snip.GetArea()
img = ImageGrab.grab(bbox=monitor)
