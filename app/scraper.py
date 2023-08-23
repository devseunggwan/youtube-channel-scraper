# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import json
import asyncio
from datetime import datetime
from typing import Any

import aiohttp
import aiofiles
from dotenv import load_dotenv


class YtChannelPlaylistsScraper:
    def __init__(self, api_key) -> None:
        self.__channel_id = str
        self.__api_key = api_key

        self.__api_host = "https://www.googleapis.com"
        self.__api_service_name = "youtube"
        self.__api_version = "v3"

        self.__api_prefix = (
            f"{self.__api_host}/{self.__api_service_name}/{self.__api_version}"
        )

    async def __write_json_file(self, data: dict) -> None:
        try:
            __date = self.__get_date()
            __time = self.__get_time()
            os.makedirs(f"output/{self.__channel_id}/{__date}", exist_ok=True)

            file_name = os.path.join(
                "output",
                self.__channel_id,
                __date,
                f"playlists_{self.__channel_id}_{__date}T{__time}.json",
            )
            async with aiofiles.open(file_name, mode="w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=4))
        except Exception as e:
            print(e)
            return False

        return True

    @staticmethod
    def __get_date() -> str:
        return datetime.now().strftime("%Y%m%d")

    @staticmethod
    def __get_time() -> str:
        return datetime.now().strftime("%H%M%S")

    async def get_playlists(self) -> list[dict[str, any]]:
        __api_name = "playlists"
        playlists = []
        next_page_token = ""
        __url = f"{self.__api_prefix}/{__api_name}?part=snippet&channelId={self.__channel_id}&maxResults=50&key={self.__api_key}"

        while True:
            async with aiohttp.ClientSession() as session:
                session_url = __url + next_page_token
                async with session.get(session_url) as response:
                    __data = await response.json()
                    playlists.extend(__data["items"])

                    if "nextPageToken" in __data:
                        next_page_token = f"&pageToken={__data['nextPageToken']}"
                    else:
                        break

        return playlists

    async def get_playlist_items(self, playlists: str) -> dict:
        __api_name = "playlistItems"
        __url = f"{self.__api_prefix}/{__api_name}?part=snippet&maxResults=50"

        playlists = await asyncio.gather(
            *[self.__request_playlist_items(playlist, __url) for playlist in playlists]
        )

        return playlists

    async def __request_playlist_items(self, playlist, session_url) -> dict[str, any]:
        next_page_token = ""
        playlist["items"] = []
        session_url = session_url + f"&playlistId={playlist['id']}"

        while True:
            async with aiohttp.ClientSession() as session:
                # api call 시 key parameter를 가장 마지막에 추가해야 합니다.
                async with session.get(
                    session_url + next_page_token + f"&key={self.__api_key}"
                ) as response:
                    __data = await response.json()
                    playlist["items"].extend(__data["items"])

                    if "nextPageToken" in __data:
                        next_page_token = f"&pageToken={__data['nextPageToken']}"
                    else:
                        break
        return playlist

    async def get_playlist_items_statistics(self, playlists):
        __api_name = "videos"
        __url = f"{self.__api_prefix}/{__api_name}?part=statistics"

        for playlist in playlists:
            for item in playlist["items"]:
                if item["snippet"]["title"] in ["Private video", "Deleted video"]:
                    continue

                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        __url
                        + f"&id={item['snippet']['resourceId']['videoId']}&key={self.__api_key}"
                    ) as response:
                        try:
                            __data = await response.json()
                            item["statistics"] = __data["items"][0]["statistics"]
                        except Exception as e:
                            print(e)
                            print(item)
                            continue

        return playlists

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.__channel_id = kwds["channel_id"]

        playlists = asyncio.run(self.get_playlists())
        playlists = asyncio.run(self.get_playlist_items(playlists))
        playlists = asyncio.run(self.get_playlist_items_statistics(playlists))

        asyncio.run(self.__write_json_file(playlists))

        return playlists
