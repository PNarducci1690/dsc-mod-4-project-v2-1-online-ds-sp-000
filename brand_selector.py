def brand_selection(tweet):
    if 'ipad' in tweet:
        return 'Apple'
    elif 'iphone' in tweet:
        return 'Apple'
    elif 'apple' in tweet:
        return 'Apple'
    elif 'google' in tweet:
        return 'Google'
    elif 'android' in tweet:
        return 'Android'
    else:
        return 'None'