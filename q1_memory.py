def q1_memory(file_path):
    import ujson
    import zipfile
    from datetime import datetime as dt
    from collections import defaultdict

    date_count=defaultdict(int)
    user_date_count=defaultdict(lambda: defaultdict(int))
    with zipfile.ZipFile(file_path, 'r') as f:
        with f.open(f.filelist[0]) as g:
            for line in g:
                tweet = ujson.loads(line)
                date_count[tweet['date'].split("T")[0]] += 1
                user_date_count[tweet['date'].split("T")[0]][tweet['user']['username']] += 1


    
    return [ 
        (dt.strptime(key,"%Y-%m-%d").date(),max(user_date_count[key],key=user_date_count[key].get))
        for key in sorted(date_count, key=date_count.get,reverse=True)[0:10]
        ]
    
