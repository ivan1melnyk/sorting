import concurrent.futures
import logging
from random import randint
from time import sleep

from pathlib import Path
import file_parser
from normalize import normalize_file, normalize_archiv

WAYS = [
    file_parser.FOLDER_PROCESS / 'images',
    file_parser.FOLDER_PROCESS / 'video',
    file_parser.FOLDER_PROCESS / 'audio',
    file_parser.FOLDER_PROCESS / 'documents',
    file_parser.FOLDER_PROCESS / 'MY_OTHER',
]

DESTINAITIONS = [
    file_parser.IMAGES,
    file_parser.VIDEO,
    file_parser.AUDIO,
    file_parser.DOCUMENTS,
    file_parser.MY_OTHER,
]

# INDEX = 0


def handle_file(INDEX):
    way = WAYS[INDEX]
    print(way.name)
    for file_name in DESTINAITIONS[INDEX]:
        way.mkdir(exist_ok=True)
        file_name.replace(way / normalize_file(file_name))
    INDEX += 1


# def handle_file(file_name: Path, target_folder: Path):
#     target_folder.mkdir(exist_ok=True)
#     file_name.replace(target_folder / normalize_file(file_name))


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(threadName)s %(message)s')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(handle_file, range(5)))
        logging.debug(results)


if __name__ == '__main__':
    file_parser.scan(file_parser.FOLDER_PROCESS)
    main()
    file_parser.del_empty_folders(file_parser.FOLDER_PROCESS)
