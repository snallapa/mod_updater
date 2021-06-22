from .base import SourceTest
from sources.github import GithubSource
import os

class TestGithub(SourceTest):

    def test_download(self):
        g = GithubSource("snallapa", "scentfindermod", self.TEST_MODS_FOLDER)
        g.download()
        self.assertTrue(os.path.exists(f"{self.TEST_MODS_FOLDER}/scentfindermod-1.8.jar"))

    def test_parse(self):
        json = {
            "owner": "snallapa",
            "repo": "scentfindermod"
        }
        g = GithubSource.parse(json, self.TEST_MODS_FOLDER, "1.16.5")
        g.download()
        self.assertTrue(os.path.exists(f"{self.TEST_MODS_FOLDER}/scentfindermod-1.8.jar"))
