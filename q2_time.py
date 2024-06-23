
def q2_time(file_path):
    
    import pandas as pd
    import emoji
    from collections import Counter
    import re
    
    df = pd.read_json(file_path, lines=True)\

    return Counter(
        (
            (
                i.chars for i in emoji.analyze(("|").join(list(df.content.values)))
                )
            )
            )\
            .most_common(10)

