def q3_time(file_path):

    import pandas as pd
    from collections import Counter
    import re

    df = pd.read_json(file_path, lines=True)
    mention_pattern=re.compile('@(\w+)')
    return Counter([i.upper() for i in re.findall(mention_pattern,("|").join(list(df.content.values)))]).most_common(10)
