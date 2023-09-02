import argparse

from app.scraper import YtChannelPlaylistsScraper

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--channel",
        type=str,
        required=True,
        help="The channel ID to scrape from.",
    )
    parser.add_argument(
        "-k",
        "--key",
        type=str,
        required=True,
        help="The API key to use for the requests.",
    )
    args = parser.parse_args()

    scraper = YtChannelPlaylistsScraper(args.key)
    result = scraper.run(args.channel)
