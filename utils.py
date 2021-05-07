import os

STATIC = 'static'


class StaticData:

    def open_file(self, filetype, filename):
        filepath = os.path.join(STATIC, filetype, filename)
        with open(filepath, 'rb') as img:
            return img.read()

    def take_img(self, imgname):
        try:
            return self.open_file('img', imgname)
        except:
            return self.open_file('img', 'icon_not_found.png')
