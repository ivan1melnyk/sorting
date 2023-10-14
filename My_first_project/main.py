from pathlib import Path
import shutil
import file_parser
from normalize import normalize_file, normalize_archiv


def handle_file(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True)
    file_name.replace(target_folder / normalize_file(file_name))

def handle_archive(file_name: Path, target_folder: Path, archive_format):
    target_folder.mkdir(exist_ok=True)
    folder_for_file = target_folder / normalize_archiv(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True)
    try:
        if archive_format == 'gz':
            archive_format = 'gztar'
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()), archive_format)
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()


#directory = Path(r'C:\Users\User\Desktop\Junk')

#file_list = [file for file in directory.iterdir()]
'''
IMAGES = ('JPEG', 'PNG', 'JPG', 'SVG')
VIDEO = ('AVI', 'MP4', 'MOV', 'MKV')
DOCUMENTS = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
AUDIO = ('MP3', 'OGG', 'WAV', 'AMR')
ARCHIVES = ('ZIP', 'GZ', 'TAR')
'''

def main():
    for file in file_parser.IMAGES:  
        handle_file(file, file_parser.FOLDER_PROCESS / 'images')
    for file in file_parser.VIDEO:  
        handle_file(file, file_parser.FOLDER_PROCESS / 'video')
    for file in file_parser.AUDIO:  
        handle_file(file, file_parser.FOLDER_PROCESS / 'audio')
    for file in file_parser.DOCUMENTS:  
        handle_file(file, file_parser.FOLDER_PROCESS / 'documents')
    for file in file_parser.MY_OTHER:  
        handle_file(file, file_parser.FOLDER_PROCESS / 'MY_OTHER')       
    for file in file_parser.ARCHIVES:  
        handle_archive(file, file_parser.FOLDER_PROCESS / 'archives', file.suffix[1:])

if __name__ == '__main__':
    file_parser.scan(file_parser.FOLDER_PROCESS)
    main()



        