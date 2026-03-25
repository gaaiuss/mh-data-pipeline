from scraper.wiki import get_monsters


def run_pipeline() -> None:
    data = get_monsters()
    print(data)


if __name__ == "__main__":
    run_pipeline()
