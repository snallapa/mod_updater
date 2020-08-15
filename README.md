# Minecraft Mod Updater

A command line tool to easily update Minecraft forge mods.

## Usage

```
mod_updater [--config config_path]
```

If no config path is given, then the default is `config.json` in the current directory.

## Config

The config describes where the mods are located so they can be downloaded easily
```json
{
    "mods_dir": "mods",
    "mods": [
        {
            "source": "GITHUB",
            "owner": "snallapa",
            "repo": "scentfindermod"
        }
    ]
}
```

### Mods Dir

The `mods_dir` is where the mods should be downloaded. For servers, this will usually be `mods` and for clients, this would be OS dependent. 

### Mod Sources

These describe where the mod should be downloaded from. As of now there is only support for `GithubSource` to download latest releases. 

```json
{
    "source": "GITHUB",
    "owner": "snallapa",
    "repo": "scentfindermod"
}
```

More sources would want to be added in the future. 

## Development

### Tests

To run the test suite, run the following in the project root directory: 
```
python -m unittest
```