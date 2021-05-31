import requests


def find_a_movie(form):

    if form.is_valid():
        search_key = form.cleaned_data.get('search', '')
        choice = form.cleaned_data.get('choice', '')

    # The requests package will generate a request with the required data:
    

    url = 'http://127.0.0.1:8000/api/imdb/?t={0}&type={1}'.format(
        search_key, choice)
    response = requests.get(url)

    # Checking for API failure
    if response.status_code == requests.codes.ok:

        # If movie was found in IMDB
        if response.json()['Response'] == 'True':

            movie_details = {
                'name': response.json()['name'],
                'genre': response.json()['genre'],
                'imdb_score': response.json()['imdb_score'],
                'director': response.json()['director'],
                'popularity': response.json()['99popularity'],
            }

        else:
            # Retrieving error message
            movie_details = {
                'error': response.json()['Error'],
                'errorstatus': True,
            }

    return movie_details


def find_many_movies(form):

    desired_movies = list()
    if form.is_valid():
        search_key = form.cleaned_data.get('search', '')
        choice = form.cleaned_data.get('choice', '')

    movies = search_key.split('+')

    # URL generated for every movie in desired_movies (list)
    # Details of for every movie stored in movie_details (dict)

    for movie in movies:
        url = 'http://127.0.0.1:8000/api/imdb/?t={0}&type={1}'.format(
            movie, choice)
        response = requests.get(url)

        if response.status_code == requests.codes.ok:
            if response.json()['Response'] == 'True':

                movie_details = {
                    'name': response.json()['name'],
                    'genre': response.json()['genre'],
                    'imdb_score': response.json()['imdb_score'],
                    'director': response.json()['director'],
                    'popularity': response.json()['99popularity'],
                }

            else:
                movie_details = {
                    'error': response.json()['Error'],
                    'errorstatus': True,
                }
            desired_movies.append(movie_details)

    return desired_movies