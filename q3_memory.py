
def q3_memory(file_path):

    import ujson
    from collections import Counter
    import re
    import zipfile


    with zipfile.ZipFile(file_path, 'r') as f:
        with f.open(f.filelist[0]) as g:
            content_list=[ujson.loads(line).get("content") for line in g]
        


    mention_pattern=re.compile('@(\w+)')
    return Counter([i.upper() for i in re.findall(mention_pattern,(' ').join(content_list))]).most_common(10)
