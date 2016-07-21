import fresh_tomatoes
import media

# Movie attributes which includes movie title, synopsis, cover art,
# and youtube video
american_beauty = media.Movie("American Beauty",
                              "Kevin Spacey plays Lester Burnham, a man in his mid-40s going through"
                               "an intense midlife crisis.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/American_Beauty_poster.jpg/220px-American_Beauty_poster.jpg",
                              "https://www.youtube.com/watch?v=3ycmmJ6rxA8",
                              "Movie: ")

inception = media.Movie("Inception",
                        "Dominick 'Dom' Cobb (Leonardo DiCaprio) and Arthur (Joseph Gordon-Levitt)"
                         "are 'extractors', who perform corporate espionage using an experimental"
                         "military technology to infiltrate the subconscious of their targets and"
                        "extract valuable information through a shared dream world.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Inception_ver3.jpg/220px-Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        "Movie: ")

empire_strikes_back = media.Movie("Star Wars: The Empire Stikes Back",
                                  "After the rebels have been brutally overpowered by the Empire on their"
                                  "newly established base, Luke Skywalker takes advanced Jedi training"
                                  "with Master Yoda, while his friends are pursued by Darth Vader as part"
                                  "of his plan to capture Luke.",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/SW_-_Empire_Strikes_Back.jpg/220px-SW_-_Empire_Strikes_Back.jpg",
                                  "https://www.youtube.com/watch?v=96v4XraJEPI",
                                  "Movie: ")

gladiator = media.Movie("Gladiator",
                        "In the final days of Marcus Aurelius' reign, the aging emperor arouses his son"
                        "Commodus' anger when he makes known his wish that Maximus be his successor.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=ol67qo3WhJk",
                        "Movie: ")

game_of_thrones = media.Tv("Game of Thrones",
                           "Rival families battle for contron of the Iron Throne in this Mediaval fantasy",
                           "https://tse3.mm.bing.net/th?id=OIP.M92f939b20a66274b15db3b2295c0bf2co0&pid=15.1",
                           "https://www.youtube.com/watch?v=EI0ib1NErqg",
                           "TV: ")

media = [american_beauty, inception, empire_strikes_back, gladiator, game_of_thrones]


# Opens movie site
fresh_tomatoes.open_movies_page(media)


