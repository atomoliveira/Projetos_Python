
from pytube import YouTube

YouTube("https://www.youtube.com/watch?v=qAoVvZEW1aU").streams.get_highest_resolution().download()