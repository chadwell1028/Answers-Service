import imgkit


class Screenshotter:

    def get_image(self, website_link):
        return imgkit.from_url(website_link, 'myfile.jpg')
