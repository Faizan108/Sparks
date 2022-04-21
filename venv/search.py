import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

youtube_data=pd.read_csv("video_result.csv")
plt.scatter(youtube_data.viewCount,youtube_data.likeCount)
