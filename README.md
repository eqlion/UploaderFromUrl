# UploaderFromUrl

This is a simple Python script that uses Yandex Disk [REST API](https://tech.yandex.com/disk/rest/) to upload file from your url to your Ya.Disk.

To get started, you need to register your app [here](https://oauth.yandex.com/client/new) and set **Yandex.Disk REST API** scope.

After that you need to obtain a token for yourself.

To upload the file, call ```upload_from_url(url, path, token)```. *url* is source url, *path* is destination folder and *token* is your token.

This script works with both Python 2 and Python 3.
