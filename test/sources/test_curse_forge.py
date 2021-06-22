from .base import SourceTest
from sources.curse_forge import CurseForgeSource
import os

class TestCurseForge(SourceTest):

    def test_download(self):
        g = CurseForgeSource("32274", "release", self.TEST_MODS_FOLDER, "1.16.5")
        g.download()
        self.assertTrue(os.path.exists(f"{self.TEST_MODS_FOLDER}/journeymap-1.16.5-5.7.1.jar"))

    def test_parse(self):
        json = {
            "project_id": "32274",
            "release_type": "release"
        }
        g = CurseForgeSource.parse(json, self.TEST_MODS_FOLDER, "1.16.5")
        g.download()
        self.assertTrue(os.path.exists(f"{self.TEST_MODS_FOLDER}/journeymap-1.16.5-5.7.1.jar"))
