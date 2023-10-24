import json

import pandas as pd
from tqdm import tqdm


class Parser:
    def __init__(self):
        pass

    @staticmethod
    def __read_json(path: str):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def __write_csv(data, path: str):
        data.to_csv(path, index=True, index_label="idx", encoding="utf-8")

        return True

    @staticmethod
    def __parse(playlists: dict) -> pd.DataFrame:
        channel_playlists_table = []

        for playlist in tqdm(playlists):
            for video in playlist["items"]:
                if video["snippet"]["title"] == "Private video":
                    continue

                channel_playlists_table.append(
                    {
                        "playlist_title": playlist["snippet"]["title"],
                        "video_title": video["snippet"]["title"],
                        "view_count": video["statistics"]["viewCount"],
                        "like_count": video["statistics"]["likeCount"],
                        "favorite_count": video["statistics"]["favoriteCount"],
                    }
                )

        return pd.DataFrame(channel_playlists_table)

    def __call__(self, path: str):
        playlists = self.__read_json(path)
        playlists = self.__parse(playlists)
        playlists = self.__write_csv(playlists, path.replace(".json", ".csv"))

        return playlists
