import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story ",
                        "A story about the boy whose toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A Sci-fi movie based on aliens",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

ratatouille = media.Movie("Ratatouille",
                          "A mouse chef",
                          "http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

homealone = media.Movie("Home Alone",
                        "A story about the boy whose toys come to life",
                        "http://4.bp.blogspot.com/-TeiCmLztI04/UJtfal9io4I/AAAAAAAAAV4/2B8-HKcgK74/s1600/Home-Alone-Mediafire.jpg",
                        "https://www.youtube.com/watch?v=CK2Btk6Ybm0")

titanic= media.Movie("Titanic",
                     "A movie about the historical ship the titanic",
                     "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                     "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

breakingDawn = media.Movie("Breaking Dawn",
                          "A movie about love between a vampire and a human",
                          "https://s-media-cache-ak0.pinimg.com/736x/43/35/dc/4335dc198196478a92558df9d7ad65f1.jpg",
                          "https://www.youtube.com/watch?v=PQNLfo-SOR4")

movies = [toy_story , avatar ,ratatouille ,homealone ,titanic ,breakingDawn]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)

