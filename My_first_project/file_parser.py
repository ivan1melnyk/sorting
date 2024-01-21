import sys
from pathlib import Path
from threading import Thread
from os import listdir
import logging

try:
    FOLDER_PROCESS = Path(sys.argv[1])
except:
    logging('Try to folder by inctance: python main.py C:\\Users\\User\\Desktop\\Хлам')
# FOLDER_PROCESS = Path(r'C:\Users\User\Desktop\Мотлох')
# FILE_DICT = {file.name: file.suffix for file in FOLDER_PROCESS.iterdir()}

IMAGES = []
VIDEO = []
AUDIO = []
DOCUMENTS = []
ARCHIVES = []

REGISTER_EXTRENTIONS = {
    'JPEG': IMAGES,
    'JPG': IMAGES,
    'PNG': IMAGES,
    'SVG': IMAGES,

    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,

    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'PDF': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,

    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,

    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
}


MY_OTHER = []
FOLDERS = []
EXTENTIONS = set()
UNKNOWN = set()
processes = []


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()


def scan(folder: Path):
    if folder.is_dir() and len(listdir(folder)) == 0:
        try:
            folder.rmdir()
            print(f"Deleted empty folder: {folder}")
            return None
        except OSError as e:
            print(f"Error deleting folder {folder}: {e}")
    # folder = Path(folder)
    logging.debug(f'Processing parser {folder.name}...')
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('images', 'archives', 'video', 'audio', 'documents', 'MY_OTHER'):
                FOLDERS.append(item)
                pr = Thread(target=scan, args=(item,))
                pr.start()
                processes.append(pr)
            continue
        extention = get_extension(item.name)  # беремо розширення
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not extention:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTRENTIONS[extention]
                ext_reg.append(full_name)
                EXTENTIONS.add(extention)
            except KeyError:
                UNKNOWN.add(extention)
                MY_OTHER.append(full_name)
    # [el.join() for el in processes]


def del_empty_folders(root_folder):
    root_path = Path(root_folder)
    for entry in root_path.rglob("*"):
        if entry.is_dir() and not any(entry.iterdir()):
            try:
                entry.rmdir()
                print(f"Deleted empty folder: {entry}")
            except OSError as e:
                print(f"Error deleting folder {entry}: {e}")


if __name__ == '__main__':
    # folder_process = sys.argv[1]
    scan(Path(FOLDER_PROCESS))

    print(f'IMAGES:      {[im.name for im in IMAGES]}')
    print(f'VIDEO:       {[vd.name for vd in VIDEO]}')
    print(f'AUDIO:       {[au.name for au in AUDIO]}')
    print(f'DOCUMENTS:   {[dc.name for dc in DOCUMENTS]}')

    print(f'Archives:    {[arch.name for arch in ARCHIVES]}')
    print(f'EXTENTIONS:  {EXTENTIONS}')
    print(f'UNKNOWN:     {UNKNOWN}')
    print(f'FOLDERS:     {[fold.name for fold in FOLDERS]}')


# if not os.listdir(path):
#    os.rmdir()
