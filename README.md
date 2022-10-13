# ftrack OpenAssetIO Plugin

A skeleton OpenAssetIO ManagerPlugin that binds ftrack to the API

> **Warning**
> This plugin is highly experimental, and subject to significant
> change.

## Getting started

To use the plugin in an OpenAssetIO host, set (or append) the
`OPENASSETIO_PLUGIN_PATH` env var to include the `python` directory in
this checkout.

The plugin requires `openassetio` to be available to python at runtime.
This is normally provided by the host tool or application (see the
[project documentation](https://github.com/OpenAssetIO/OpenAssetIO#getting-started)
for more information if you need to install yourself).

The plugin provides a manager with the identifier `com.ftrack`.

## Testing

The test fixtures take care of configuring the OpenAssetIO plugin search
paths for you. Assuming your working directory is set to the root of
this checkout:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r tests/requirements.txt
pytest
```
