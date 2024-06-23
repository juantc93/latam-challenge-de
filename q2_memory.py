
def q2_memory(file_path):

    import ujson
    import emoji
    from collections import Counter
    import re
    import zipfile


    with zipfile.ZipFile(file_path, 'r') as f:
        with f.open(f.filelist[0]) as g:
            content_list=[ujson.loads(line).get("content") for line in g]

    return Counter(
        (
            (
                i.chars for i in emoji.analyze(("|").join(content_list))
                )
            )
            )\
            .most_common(10)
