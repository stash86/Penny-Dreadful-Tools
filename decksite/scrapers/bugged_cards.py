from magic import multiverse


def scrape() -> None:
    multiverse.update_bugged_cards()
    multiverse.update_cache()
