import shutil
import os
import datetime

def backup_file(source,destination):
    today = datetime.date.today()
    # backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz")
    # shutil.make_archive(backup_file_name.replace('.tar.gz',''),'gztar',source)\
    backup_file_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)

source = "/home/nimap/uday/Programming/Python"
destination = "/home/nimap/uday/Programming/Python/backups"
backup_file(source,destination)