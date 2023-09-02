# youtube-channel-scraper

Youtube 내 채널 별 재생목록과 동영상 정보들을 전부 가져옵니다. 

Youtube API V3를 사용하여 가져오며, 사용한 API는 다음과 같습니다.

* [Playlist 조회](https://developers.google.com/youtube/v3/docs/playlists/list?hl=ko)
* [Playlist 내 동영상 조회](https://developers.google.com/youtube/v3/docs/playlistItems/list?hl=ko)
* [동영상 조회수, 좋아요 조회](https://developers.google.com/youtube/v3/docs/videos/list?hl=ko)

## Quickstart

### API Key 발급

* Scraper에 사용되는 Youtube API V3를 사용하기 위해선 해당 API 사용이 승인된 Key가 필요합니다.
* API Key를 발급받기 위해서 아래의 Reference 를 참조바랍니다.
  * https://developers.google.com/youtube/v3/getting-started?hl=ko

### Python 환경 설치

> 해당 환경 설정은 Github Codespace 기준으로 제작되었습니다. 다른 곳에서 사용해도 무방하나 일부 환경에서는 동작하지 않을 수 있습니다.

```shell
sh .project-env-setting.sh
```

### Scraping 코드 실행

```shell
python main.py --key {YOUR-API-KEY} --channel {CHANNEL-ID}
```

## Output

### Folder 구조

```
output
└──{CHANNEL-ID}
	   ├──{YYYYMMDD}
	   │		├──playlists_{CHANNEL-ID}_{YYYYMMDDTHHMMSS}.json
	   │		├──playlists_{CHANNEL-ID}_{YYYYMMDDTHHMMSS}.json
	   │		└──playlists_{CHANNEL-ID}_{YYYYMMDDTHHMMSS}.json
	   └──{YYYYMMDD}
  		 		├──playlists_{CHANNEL-ID}_{YYYYMMDDTHHMMSS}.json
   				├──playlists_{CHANNEL-ID}_{YYYYMMDDTHHMMSS}.json
   				└──playlists_{CHANNEL-ID}_{YYYYMMDDTHHMMSS}.json
```

### Json 구조

```
{
    "kind": "youtube#playlist",
    "etag": "",
    "id": "",
    "snippet": {
        "publishedAt": "2023-07-30T11:07:01Z",
        "channelId": "",
        "title": "",
        "description": "",
        "thumbnails": {
            "default": {
                "url": "",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "",
                "width": 480,
                "height": 360
            },
            "standard": {
                "url": "",
                "width": 640,
                "height": 480
            },
            "maxres": {
                "url": "",
                "width": 1280,
                "height": 720
            }
        },
        "channelTitle": "",
        "localized": {
            "title": "",
            "description": ""
        }
    },
    "items": [
        {
            "kind": "youtube#playlistItem",
            "etag": "",
            "id": "",
            "snippet": {
                "publishedAt": "2023-07-30T11:07:07Z",
                "channelId": "",
                "title": "",
                "description": "",
                "thumbnails": {
                    "default": {
                        "url": "",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "",
                        "width": 480,
                        "height": 360
                    },
                    "standard": {
                        "url": "",
                        "width": 640,
                        "height": 480
                    },
                    "maxres": {
                        "url": "",
                        "width": 1280,
                        "height": 720
                    }
                },
                "channelTitle": "",
                "playlistId": "",
                "position": 0,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": ""
                },
                "videoOwnerChannelTitle": "",
                "videoOwnerChannelId": ""
            },
            "statistics": {
                "viewCount": "25976",
                "likeCount": "561",
                "favoriteCount": "0"
            },
            "transcript": [
                {
                    "text": "",
                    "start": 3.08,
                    "duration": 4.2
                }
            ]
        }
    ]
}
```



## Scraper 관련 문의

* Issue 작성 부탁드립니다 👋
