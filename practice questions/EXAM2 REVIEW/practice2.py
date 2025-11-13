def summarize_book_ratings(library, book_title):
    min_val = 6
    max_val = 0
    avg = 0
    ratings = []
    for lib, info in library.items():
        if book_title in info:
            value = sum(info[book_title]/len(book_title))
            if min(info[book_title]) < min_val:
                min_val = min(info[book_title])
            if max(info[book_title]) > max_val:
                max_val = max(info[book_title])
            ratings.append(value)

    return min_val, max_val, round(sum(ratings/len(ratings), 1))
