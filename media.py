
class Movie():
    """this class is the base class for the movie project """
    VALID_RATINGS= ["G" , "PG" , "PG-13" , "R"]
    def __init__(self, movie_trailer,movie_story_line,poster_image_url,trailer_youtube_url):
        self.title = movie_trailer
        self.story_line = movie_story_line,
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

