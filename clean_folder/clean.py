import shutil
from pathlib import Path
from clean_folder.normal import normalize
import sys

def sorting():
    folder = sys.argv[-1]
    img = ('JPEG', 'PNG', 'JPG', 'SVG')
    vid = ('AVI', 'MP4', 'MOV', 'MKV')
    doc = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    muz = ('MP3', 'OGG', 'WAV', 'AMR')
    arch = ('ZIP', 'GZ', 'TAR')

    Path(folder + '/' + 'images').mkdir(exist_ok=True)
    Path(folder + '/' + 'video').mkdir(exist_ok=True)
    Path(folder + '/' + 'documents').mkdir(exist_ok=True)
    Path(folder + '/' + 'audio').mkdir(exist_ok=True)
    Path(folder + '/' + 'archives').mkdir(exist_ok=True)

    for i in Path(folder).glob('**\*'):

        if i.name == 'images' or i.name == 'video' or i.name == 'documents' or i.name == 'audio' or i.name == 'archives':
            continue
        if i.is_dir():
            continue
        if i.suffix.upper()[1:] in img:
            Path(i).rename(r'D:\trash\images'+'\\' + normalize(i.name))
        elif i.suffix.upper()[1:] in vid:
            Path(i).rename(r'D:\trash\video'+'\\' + normalize(i.name))
        elif i.suffix.upper()[1:] in doc:
            Path(i).rename(r'D:\trash\documents'+'\\' + normalize(i.name))
        elif i.suffix.upper()[1:] in muz:
            Path(i).rename(r'D:\trash\audio'+'\\' + normalize(i.name))
        elif i.suffix.upper()[1:] in arch:
            try:
                shutil.unpack_archive(
                    Path(i), r'D:\trash\archives' + '\\' + normalize(i.name))
            except:
                continue

    for empty in Path(folder).glob('**/*'):
        if empty.is_dir() and not list(empty.glob('*')):
            empty.rmdir()


# if __name__ == '__main__':
#     sorting(sys.argv[-1])
