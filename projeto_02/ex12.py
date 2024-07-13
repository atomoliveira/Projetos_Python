
from pytube import YouTube

YouTube("https://www.youtube.com/watch?v=kCMaqla6Grs&list=PLpdAy0tYrnKx9CtTmgSdzHz9YQ-C5ZNI9").streams.get_highest_resolution().download()