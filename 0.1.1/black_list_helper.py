cached_blacklist = None

def get_blacklist_from_string(banwords=None):
    global cached_blacklist

    if cached_blacklist is not None:
        return cached_blacklist

    if banwords is not None:
        cached_blacklist = [word.strip() for word in banwords.splitlines()]
        return cached_blacklist

    return cached_blacklist