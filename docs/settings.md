# `settings` class

We use a the `settings` class from [settings.py](https://github.com/pixiee-ai/pixy-sdk/blob/main/src/pixy/settings.py) to store the settings that pixy SDK relies on; currently, these settings include:

1. **url_mapping** (dict): The URL mapping to determine the endpoint, given the `generation_type`; stick to the default value, unless you have a custom provider.
2. **properties_mapping** (dict): The properties mapping to determine the type of the `properties`, given the `generation_type`; stick to the default value, unless you have a custom provider.

This class is initialized with the default values; therefore, unless you are using a custom provider, you don't need to worry about the values it contains. Moreover, as this class is a static class, its attributes are accessible without instantiating it.

In case you are using a custom provider, you are supposed to instanciate from this class with custom endpoints, as below:

```python

from pixy.settings import Settings

settings = Settings(
    url_mapping = {"image": "https://example.com/image",
                  "video": "https://example.com/video",
                  "subtitle": "https://example.com/subtitle"},
)

```

Don't forget to pass the custom settings to the `PixyClient` class, as well. You are supposed to this, once instanciating from the `PixyClient` class:

```python
from pixy.client import PixyClient

# assuming that you have declared the custom settings above

client = PixyClient(api_key, settings)

```

You also need to pass the attributes from the custom `settings` class to the functions from the `pixy.utils` module, as well; checkout the [utils documentation](https://github.com/pixiee-ai/pixy-sdk/blob/main/docs/utils.md) for more details.