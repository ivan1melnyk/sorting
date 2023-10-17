import sys
from pathlib import Path

FOLDER_PROCESS = sys.argv[1]
#FOLDER_PROCESS = Path(r'C:\Users\User\Desktop\Мотлох')
#FILE_DICT = {file.name: file.suffix for file in FOLDER_PROCESS.iterdir()}

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

def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()

def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('images', 'archives', 'video', 'audio', 'documents', 'MY_OTHER'):
                FOLDERS.append(item)
                try:
                    item.rmdir()
                except:
                    scan(item)
            continue
        extention = get_extension(item.name)   #беремо розширення
        full_name = folder / item.name         #беремо повний шлях до файлу
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


if __name__ == '__main__':
    #folder_process = sys.argv[1]
    scan(Path(FOLDER_PROCESS))

    print(f'IMAGES:      {[im.name for im in IMAGES]}')
    print(f'VIDEO:       {[vd.name for vd in VIDEO]}')
    print(f'AUDIO:       {[au.name for au in AUDIO]}')
    print(f'DOCUMENTS:   {[dc.name for dc in DOCUMENTS]}')

    print(f'Archives:    {[arch.name for arch in ARCHIVES]}')
    print(f'EXTENTIONS:  {EXTENTIONS}')
    print(f'UNKNOWN:     {UNKNOWN}')
    print(f'FOLDERS:     {[fold.name for fold in FOLDERS]}')



#if not os.listdir(path): 
#    os.rmdir()
