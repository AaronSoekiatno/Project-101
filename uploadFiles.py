import dropbox
import os

class TransferFiles:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, file in os.walk(file_from):
            for fileName in file:
                local_path = os.path.join(root, fileName)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
def main():
    access_token = "VKzf6WgB7-oAAAAAAAAAAVwyk2x3EqxQLVTrhGCrfF4608iqF4tsBagRi7r2Bj-0"
    transferData = TransferFiles(access_token)
    file_from = "sample2.txt"
    file_to = "/home/Test/sample2.txt"
    transferData.upload_file(file_from,file_to)
    print("Your file has been transfered")
main()
