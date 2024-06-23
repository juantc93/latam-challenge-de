def q1_time(file_path):
    import pandas as pd
    df = pd.read_json(file_path, lines=True)\
        .assign(date=lambda x: x.date.dt.date,
                username=lambda x: x.user.apply(lambda y: y.get("username")))

    df_top_ten_date=df["date"]\
        .value_counts()\
        .nlargest(10)\
        .rename("twits")\
        .rename_axis("date")


    return df.loc[:,["date","username"]]\
        .set_index("date")\
        .join(df_top_ten_date,how="inner")\
        .set_index("username",append=True)\
        .groupby(["date","username","twits"])\
        .agg(twits_user=pd.NamedAgg(column="twits",aggfunc="count"))\
        .assign(
            rank=lambda x: x.groupby(["date","twits"])["twits_user"].rank(axis='index',method="first",ascending=False))\
        .query("rank==1")\
        .sort_index(level="twits",ascending=False)\
        .reset_index()\
        .loc[:,["date","username"]]\
        .to_records(index=False).tolist()

