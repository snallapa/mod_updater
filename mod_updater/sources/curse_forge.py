from .base import DownloadSource
import requests
from mod_updater.util.utils import TermColors

class CurseForgeSource(DownloadSource):
    REQUIRED_ARGS = ["project_id"]
    OPTIONAL_ARGS = [("release_type", "release")]
    
    def __init__(self, project, release_type, path, mc_version):
        self._file_data_url = f"https://api.cfwidget.com/minecraft/mc-mods/{project}"
        self._release_type = release_type
        self._path = path
        self._mc_version = mc_version

    def download(self):
        r = requests.get(self._file_data_url)
        files = r.json()["files"]
        def isTargetFile(f):
            return f["type"] == self._release_type and self._mc_version in f["versions"]
        targetFileHuh = list(filter(isTargetFile, files))
        if len(targetFileHuh) < 1:
            # print(f"{TermColors.FAIL}did not found target file in {r.json()} {TermColors.ENDC}")
            raise Exception("failed to find a file")
        if len(targetFileHuh) > 1:
            print(f"{TermColors.WARNING}WARNING, multiple curse forge file found, choosing the first one{TermColors.ENDC}")
        targetFile = targetFileHuh[0]
        file_id = str(targetFile["id"])
        asset_name = str(targetFile["name"])
        download_url = f"https://media.forgecdn.net/files/{file_id[0:4]}/{file_id[4:]}/{asset_name}"
        download_response = requests.get(download_url, stream=True)
        self.download_file(download_response, f"{self._path}/{asset_name}")

    @classmethod
    def parse(cls, json, path, mc_version):
        for arg in cls.REQUIRED_ARGS:
            if arg not in json:
                raise Exception("Missing required arg ", arg, "in ", json)
        for (arg, default) in cls.OPTIONAL_ARGS:
            if arg not in json:
                json[arg] = default
        project = json["project_id"]
        release_type = json["release_type"]
        return cls(project, release_type, path, mc_version)
