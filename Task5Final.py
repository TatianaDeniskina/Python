import urllib.request
import chardet
rawdata = urllib.request.urlopen('http://yandex.ru/').read()
print(chardet.detect(rawdata))
rawdata = urllib.request.urlopen('http://youtube.com/').read()
print(chardet.detect(rawdata))

