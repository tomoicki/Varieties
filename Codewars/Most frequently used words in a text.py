def top_3_words(text):
    text = text.lower()
    unwanteds = [',','.','/','-',';','!','?','_',':']
    max_list = []
    number_of_keys = 0
    splitted = text
    for sign in unwanteds:
        splitted = splitted.replace(sign,' ')
    splitted = splitted.split()
    for word in splitted:
        if len(word) == word.count('\''):
            while word in splitted: splitted.remove(word)
    counts = {}
    for word in splitted:
        up = {word:splitted.count(word)}
        counts.update(up)
    for key in counts:
        number_of_keys +=1
    if number_of_keys > 3: number_of_keys = 3
    for x in range(number_of_keys):
        max_key = max(counts, key=counts.get)
        max_list.append(max_key)
        del counts[max_key]
    return max_list

# alternative solutions
#
# from collections import Counter
# import re
# def top_3_words(text):
#     c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
#     return [w for w,_ in c.most_common(3)]
#
# import re
# from collections import Counter
# top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]