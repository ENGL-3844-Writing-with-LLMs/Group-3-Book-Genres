# %%
import pandas as pd

# %%
df = pd.read_csv('../Final_Project/data.csv', delimiter=',', encoding='utf-8')

# adds two addtional columns containing the length of the book's summary and title
df['title_length'] = df.title.apply(len)
df['summary_length'] = df.summary.apply(len)
df['title_duplicates'] = df.title.duplicated()
df['summery_duplicates'] = df.summary.duplicated()

# %%
df.shape

# %%
df.info()

# %% [markdown]
# Observations:
# (1) There do not appear to be any missing data for any of the columns. 

# %%
df.columns

# %%
df.title.describe()

# %%
duplicate_titles = df.groupby('title').count()['duplicates'].sort_values(ascending=False)
duplicate_titles

# %%
duplicates_of_4 = len([count for count in duplicate_titles if count == 4])
duplicates_of_3 = len([count for count in duplicate_titles if count == 3])
duplicates_of_2 = len([count for count in duplicate_titles if count == 2])

print(f"Number of titles with 4 duplicates: {duplicates_of_4}")
print(f"Number of titles with 3 duplicates: {duplicates_of_3}")
print(f"Number of titles with 2 duplicates: {duplicates_of_2}")

# %% [markdown]
# Observations: 
# 
# (1) The data does not contain solely unique entries for the title of its novels, specifically, there exist 361 title duplicates. Moreover, these duplicate entries are not necessarily identical. For example, the title "Hunger Games" appears 4 times in the data set. However, 3 of these entries provide the same cited summaries, while 1 appears to be a much lengthier version detailing the entire events of the novel. Addtionally, the genre descriptions of the duplicated entries also differ despite the fact that most shared the same cited summary. In total, "Hunger Games" was labelled as a science, romance, and fantasy centered novel.
# 
# (2) Most duplicate titles are only duplicated once, with a few (although not insignificant amount) being duplicated twice or three times. 
# 
# (3) The most commonly duplicated titles consist of only one (arguable common occuring) word, such as "Broken", "Bloodline", or "Annihiliation". 

# %%
df.summary.describe()

# %% [markdown]
# Observations:
# 
# (1) Similar to the title column, there appears to be duplicated summaries. However, it's worth noting that the number of duplicates among the titles and summaries vastly differ, with there being only 115 duplicate summaries. This seems to suggest that a portion of duplicated titles could be conicidences. Namely, it could be the case that multiple, different novels just so happen to share the same title. In fact, after some investigation, it appears that this assumption is correct (at least for certain entries). For example, the title "Bloodline" has 4 total entries. However, each is for a separate novel. The same is true for the title "Nemesis". 
# 
# (2)
# 

# %%
df.genre.describe()

# %%
df.genre.value_counts().describe()

# %%
df.genre.value_counts().plot(kind='bar')

# %% [markdown]
# Observations:
# 
# (1) Thriller is the most commonly occuring genre included in the data set, while travel is the rarest. 
# 
# (2) The distribution of the genres appear to be grouped into 3 primary concentrations, i.e., {thriller, fantasy}, {science, history, horror, crime}, and {romance, psychology, sports, travel}. Moreover, these concentrations significantly differ in their frequency, with the standard deviation between the frequency of all genres being 345.77. 
# 
# (3) The least represented genres are mostly compromised of non-fiction categories like psychology, sports, and travel, which may introduce an additional layer of difference between them and other genres. 
# 
# (4) The most popular genres appear to very broadily defined, such as thriller which can be seen as having many overlapping qualities with fantasy and science. 
# 
# (5) The genres themselves do not appear to be very well-defined. For instance, does the genres of science and history contain a mixture of both fiction and non-fiction, or are they only inclusive towards one? (EDIT: There appears to be a mixture)

# %%
df.title_length.describe()

# %%
df.title_length.hist(
    figsize=(12, 8)
)

# %% [markdown]
# Observations:
# 
# (1) The distribution of title lengths is generally centered around 0-25 words, with the overall mean being 19.3.
# 
# (2) Relative to the mean, the standard devation (14.6) is rather high, especially since 75% of the title lengths fall below 21 words. Although somewhat evident from the histogram, this seems to indicate that that there are multiple outliers skewing the data towards larger results. 
# 
# (3) The max title length is a definitive outlier at 166 words. As such, it's (and other lengthy title entries') exclusion should be considered. However, it should first be evaluated whether certain genres have a pattern of possessing these longer titles, as excluding them under such a situation could one-sidedly affect the accuracy of predicting certain genres. 
# 

# %%
df.summary_length.describe()

# %%
df.summary_length.hist(
    figsize=(12, 8)
)


