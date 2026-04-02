#!/usr/bin/env python3
import json
import os
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: python create_movie_subtitle_json.py <imdb_id> <base_url> <subtitle_filename>")
        print("Example: python create_movie_subtitle_json.py tt1375666 https://alonlevinzon.github.io/stremio-he-subtitles tt1375666.he.srt")
        sys.exit(1)

    imdb_id = sys.argv[1].strip()
    base_url = sys.argv[2].rstrip("/")
    subtitle_filename = sys.argv[3].strip()

    os.makedirs("subtitles/movie", exist_ok=True)
    output_path = os.path.join("subtitles", "movie", f"{imdb_id}.json")

    data = {
        "subtitles": [
            {
                "id": f"{imdb_id}-he-1",
                "lang": "heb",
                "url": f"{base_url}/files/{subtitle_filename}"
            }
        ],
        "cacheMaxAge": 300,
        "staleRevalidate": 3600,
        "staleError": 86400
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Created {output_path}")


if __name__ == "__main__":
    main()
