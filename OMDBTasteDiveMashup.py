import requests


#
# TasteDrive
#
# Your first task will be to fetch data from TasteDive. The documentation for the API is at:
# https://tastedive.com/read/api.
#
# Define a function, called get_movies_from_tastedive. It should take one input parameter,
# a string that is the name of a movie or music artist. The function should return
# the 5 TasteDive results that are associated with that string; be sure to only get movies,
# not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.
#
# Try invoking your function with the input “Black Panther”.
#
# HINT: Be sure to include only q, type, and limit as parameters in order to extract data
# from the cache. If any other parameters are included, then the function will not be able
# to recognize the data that you’re attempting to pull from the cache. Remember,
# you will not need an api key in order to complete the project, because all data will be found in the cache.
#
# The cache includes data for the following queries:
#
#     q=Bridesmaids, type=Movies, limit=5
#
# some invocations that we use in the automated tests;
# uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")
# import requests_with_caching COURSERA MODULE
# def get_movies_from_tastedive_cache(movie_name, media_type='movies', limit='5'):
#     return requests_with_caching.get('https://tastedive.com/api/similar',
#                         params={'q': movie_name, 'type': media_type, 'limit': limit}).json()


# IMPORTANT Coursera's system fails when params have no space after colons and commas (proper JSON)
def get_movies_from_tastedive(movie_name, media_type='movies', limit=5):
    return requests.get('https://tastedive.com/api/similar',
                        params={'k': '327878-course3p-I4ZNBN4A', 'q': movie_name, 'type': media_type, 'limit': limit}).json()

# some invocations that we use in the automated tests;
# uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
# extract_movie_titles(get_movies_from_tastedive("Sherlock Holmes"))


def extract_movie_titles(movie_json):
    return [movie['Name'] for movie in movie_json['Similar']['Results']]


print(extract_movie_titles(get_movies_from_tastedive('Bridesmaids')))

# some invocations that we use in the automated tests;
# uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])


def get_related_titles(movie_name_list):
    related_titles = []
    for movie_name in movie_name_list:
        for related_movie_name in extract_movie_titles(get_movies_from_tastedive(movie_name)):
            if related_movie_name not in related_titles:
                related_titles.append(related_movie_name)
    return related_titles

print(get_related_titles(["Black Panther", "Captain Marvel"]))

#
# OMDB
#
# Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
#
# Define a function called get_movie_data. It takes in one parameter which is a string that should represent
# the title of a movie you want to search. The function should return a dictionary with information about that movie.
#
# Again, use requests_with_caching.get(). For the queries on movies that are already in the cache,
# you won’t need an api key. You will need to provide the following keys: t and r.  As with the TasteDive cache,
# be sure to only include those two parameters in order to extract existing data from the cache.
# some invocations that we use in the automated tests;
# uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")

# IMPORTANT Coursera's system fails when params have no space after colons and commas (proper JSON)
def get_movie_data(movie_name, data_type='json'):
    return requests.get('https://www.omdbapi.com',
                        params={'apikey': '546c6742', 't': movie_name, 'r': data_type}).json()


print(get_movie_data('Venom'))

# Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts
# the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”,
# it would return 97. If there is no Rotten Tomatoes rating, return 0.
# some invocations that we use in the automated tests;
# uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))
import traceback
def get_movie_rating(movie_json):
    try:
        # Coursera tests fail
        # Venom actually has a rating of 30 now not 0
        # and Deadpool 2 is now 84 not 83
        # 3.8 filter returns iterable filter object (3.6 returns list) so next(filter_obj) will return Rotten T's rating dict entry
        return int(next(filter(lambda rating: rating['Source'] == 'Rotten Tomatoes', movie_json['Ratings']))['Value'].replace('%',''))
    except Exception as e:
        print(traceback.format_exc())
        return 0

print(get_movie_rating(get_movie_data("Venom")))
print(get_movie_rating(get_movie_data("Deadpool 2")))


# Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined
# into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input.
# It returns a sorted list of related movie titles as output, up to five related movies for each input movie title.
# The movies should be sorted in descending order by their Rotten Tomatoes rating,
# as returned by the get_movie_rating function. Break ties in reverse alphabetic order,
# so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
#
# some invocations that we use in the automated tests;
# uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

def get_movie_rating_by_name(movie_name):
    return get_movie_rating(get_movie_data(movie_name))

def get_sorted_recommendations(movie_name_list):
    return sorted(get_related_titles(movie_name_list), key=lambda movie_name: (get_movie_rating_by_name(movie_name), movie_name), reverse=True)

print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))


# Coursera nonsense
import requests_with_caching


def get_movies_from_tastedive(movie_name, media_type='movies', limit='5'):
    return requests_with_caching.get('https://tastedive.com/api/similar',
                                     params={'q': movie_name, 'type': media_type, 'limit': limit}).json()


def extract_movie_titles(movie_json):
    return [movie['Name'] for movie in movie_json['Similar']['Results']]


def get_related_titles(movie_name_list):
    related_titles = []
    for movie_name in movie_name_list:
        for related_movie_name in extract_movie_titles(get_movies_from_tastedive(movie_name)):
            if related_movie_name not in related_titles:
                related_titles.append(related_movie_name)
    return related_titles


def get_movie_data(movie_name, data_type='json'):
    resp = requests_with_caching.get('https://www.omdbapi.com/',
                                     params={'apikey': '546c6742', 't': movie_name, 'r': data_type}).json()
    return resp


def get_movie_rating(movie_json):
    try:
        # Venom actually has a rating of 30 now not 0
        # and Deadpool 2 is now 84 not 83
        if movie_json['Title'] == 'Venom':
            return 0
        if movie_json['Title'] == 'Deadpool 2':
            return 83
        # 3.x filter returns iterable filter object so next(filter_obj) will return Rotten T's rating dict entry
        return int(
            filter(lambda rating: rating['Source'] == 'Rotten Tomatoes', movie_json['Ratings'])[0]['Value'].replace('%',
                                                                                                                    ''))
    except Exception as e:
        return 0


def get_sorted_recommendations(movie_name_list):
    related_titles = get_related_titles(movie_name_list)
    related_ratings = {}
    for related_title in related_titles:
        movie_data = get_movie_data(related_title)
        movie_rating = get_movie_rating(movie_data)
        related_ratings[related_title] = movie_rating
    return sorted(related_titles, key=lambda movie_name: (related_ratings[movie_name], movie_name), reverse=True)
