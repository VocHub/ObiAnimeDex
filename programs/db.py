import requests


def update_views(anime):
    try:
        requests.get("https://animedex-api.herokuapp.com/db/view?anime=" + anime.strip())
    except:
        pass
    return


def update_watch(anime):
    try:
        requests.get("https://animedex-api.herokuapp.com/db/watch?anime=" + anime.strip())
    except:
        pass
    return
