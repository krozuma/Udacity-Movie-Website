import webbrowser


class Media:
    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, type_of):
        self.title = media_title
        self.storyline = media_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.type_of = type_of


class Movie(Media):
    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, type_of):
        Media.__init__(self, media_title, media_storyline, poster_image, trailer_youtube, type_of)


class Tv(Media):
    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, type_of):
        Media.__init__(self, media_title, media_storyline, poster_image, trailer_youtube, type_of)
        
# Function opens and plays movie trailers.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
