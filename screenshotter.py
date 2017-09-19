import imgkit


class Screenshotter:

    def __init__(self, website_link):

        imgkit.from_url(website_link, 'test.png')
