# PixyClient API Reference

The easiest approach to use the Pixy SDK is to initialize a new instance of the PixyClient class, using the API key obtained from the Pixy panel. In this page, we walk through the whole functionalities of the PixyClient class, step by step.

## Usage

### 1. ```PixyClient(api_key: str, settings: Settings = Settings)```

#### Description:
Initializes a new instance of the PixyClient class, given the API key. The API key is verified automatically.

#### Args:
* api_key (str): The API key obtained from the Pixy panel.
* settings (Settings): The settings to use; stick to the default value, unless you have a custom provider. Checkout the [settings documentation]() for a comprehensive instruction on how to declare custom settings.

#### Example:
```python

from client import PixyClient

api_key = "your_api_key"
client = PixyClient(api_key)

>>> API key is verified successfully.
```

### ```PixyClient.generate(generation_type: str, properties: ImageGenProperties | VideoGenProperties | SubtitleGenProperties) -> dict```

#### Description:
Generates a resource (image, video, subtitle) based on the given properties.

#### Args:
* generation_type (str): The type of resource to generate; valid choices are: `"image"`, `"video"`, `"subtitle"`.
* properties (ImageGenProperties | VideoGenProperties | SubtitleGenProperties): The properties to generate the resource with; notice that the properties must match the type of resource to generate.

#### Returns:
* dict: A JSON response containing the generated resource.

#### Example:
```python

from client import PixyClient
from core.schemas import ImageGenProperties

api_key = "your_api_key"
client = PixyClient(api_key)

properties = ImageGenProperties(
    engine = "photon_flash",
    aspect_ratio = "1:1",
    delineation = "a red kite flying over the sea",
    context = [{}],
    enhance_prompt = True
)

resource = client.generate("image", properties)

>>>{
>>>  "created_at": "2025-04-08T09:08:45.129Z",
>>>  "updated_at": "2025-04-08T09:08:45.129Z",
>>>  "is_deleted": false,
>>>  "meta_data": {},
>>>  "uid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
>>>  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
>>>  "task_status": "draft",
>>>  "task_report": "string",
>>>  "task_progress": -1,
>>>  "task_logs": [],
>>>  "task_references": {
>>>    "tasks": [],
>>>    "mode": "serial"
>>>  },
>>>  "task_start_at": "2025-04-08T09:08:45.129Z",
>>>  "task_end_at": "2025-04-08T09:08:45.129Z",
>>>  "webhook_url": "string",
>>>  "engine": "photon_flash",
>>>  "aspect_ratio": "1:1",
>>>  "delineation": "a red kite flying over the sea",
>>>  "context": [
>>>    {}
>>>  ],
>>>  "enhance_prompt": True,
>>>  "prompt": "string",
>>>  "error": "string",
>>>  "bulk": "string",
>>>  "status": "init",
>>>  "results": [
>>>    {
>>>      "url": "string",
>>>      "width": 0,
>>>      "height": 0
>>>    }
>>>  ],
>>>  "usage_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
>>>}
```

### ```PixyClient.get_by_uid(generation_type: str, uid: str) -> dict```

#### Description:
Retrieves a resource by its unique identifier.

#### Args:
* generation_type (str): The type of resource to retrieve.
* uid (str): The unique identifier of the resource.

#### Returns:
* dict: A JSON response containing the retrieved resource.

#### Example:
```python
from client import PixyClient

api_key = "your_api_key"
client = PixyClient(api_key)

resource = client.get_by_uid("image", "desired_uid")

print(resource)

>>>{
>>>  "created_at": "2025-04-08T09:50:20.518Z",
>>>  "updated_at": "2025-04-08T09:50:20.518Z",
>>>  "is_deleted": false,
>>>  "meta_data": {},
>>>  "uid": "desired_UID",
>>>  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
>>>  "task_status": "draft",
>>>  "task_report": "string",
>>>  "task_progress": -1,
>>>  "task_logs": [],
>>>  "task_references": {
>>>    "tasks": [],
>>>    "mode": "serial"
>>>  },
>>>  "task_start_at": "2025-04-08T09:50:20.518Z",
>>>  "task_end_at": "2025-04-08T09:50:20.518Z",
>>>  "webhook_url": "string",
>>>  "engine": "flux_schnell",
>>>  "aspect_ratio": "1:1",
>>>  "delineation": "string",
>>>  "context": [
>>>    {}
>>>  ],
>>>  "enhance_prompt": false,
>>>  "prompt": "string",
>>>  "error": "string",
>>>  "bulk": "string",
>>>  "status": "init",
>>>  "results": [
>>>    {
>>>      "url": "string",
>>>      "width": 0,
>>>      "height": 0
>>>    }
>>>  ],
>>>  "usage_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
>>>}
```

### ```PixyClient.get_list(generation_type: str, params: GetListParameters) -> dict```

#### Description:
Retrieves a resource by its status.

#### Args:
* generation_type (str): The type of resource to retrieve.
* status (str): The status of the resource.

#### Returns:
* dict: A JSON response containing the retrieved resource.

#### Example:
```python
from client import PixyClient
from core.models import GetListParameters

api_key = "your_api_key"    
client = PixyClient(api_key)

params = GetListParameters(
    offset = 0,
    limit = 2,
    created_at_from = "2025-02-01T00:00:00.000000",
    created_at_to = "2025-05-01T00:00:00.000000",
)

resource = client.get_list("image", params)

print(resource)

{
  "items": [
    {
      "created_at": "2025-04-03T16:55:01.462000",
      "updated_at": "2025-04-03T16:59:15.805000",
      "is_deleted": False,
      "meta_data": None,
      "uid": "69a56ee2-015a-4b52-b492-e5a006a1c5cd",
      "user_id": "b437e434-c965-4a11-88d8-5fe950dbcffd",
      "task_status": "error",
      "task_report": "Imagine failed, 'NoneType' object has no attribute 'get'",
      "task_progress": -1,
      "task_logs": [
        {
          "reported_at": "2025-04-03T16:59:15.805000",
          "message": "Imagine failed, 'NoneType' object has no attribute 'get'",
          "task_status": "error",
          "duration": 0,
          "log_type": "error"
        }
      ],
      "task_references": None,
      "task_start_at": None,
      "task_end_at": None,
      "webhook_url": None,
      "engine": "photon_flash",
      "aspect_ratio": "1:1",
      "delineation": None,
      "context": [
        {}
      ],
      "enhance_prompt": False,
      "prompt": None,
      "error": "'NoneType' object has no attribute 'get'",
      "bulk": None,
      "status": "error",
      "results": None,
      "usage_id": None
    },
    {
      "created_at": "2025-04-03T12:26:01.705000",
      "updated_at": "2025-04-03T12:29:15.810000",
      "is_deleted": False,
      "meta_data": None,
      "uid": "719f2836-1905-4061-a143-9c2b02453192",
      "user_id": "b437e434-c965-4a11-88d8-5fe950dbcffd",
      "task_status": "error",
      "task_report": "Imagine failed, 'NoneType' object has no attribute 'get'",
      "task_progress": -1,
      "task_logs": [
        {
          "reported_at": "2025-04-03T12:29:15.809000",
          "message": "Imagine failed, 'NoneType' object has no attribute 'get'",
          "task_status": "error",
          "duration": 0,
          "log_type": "error"
        }
      ],
      "task_references": None,
      "task_start_at": None,
      "task_end_at": None,
      "webhook_url": None,
      "engine": "photon_flash",
      "aspect_ratio": "1:1",
      "delineation": None,
      "context": [
        {}
      ],
      "enhance_prompt": False,
      "prompt": None,
      "error": "'NoneType' object has no attribute 'get'",
      "bulk": None,
      "status": "error",
      "results": None,
      "usage_id": None
    }
  ],
  "total": 256,
  "offset": 0,
  "limit": 2
}
```

### ```PixyClient.delete(generation_type: str, uid: str) -> dict```

#### Description:
Deletes a resource by its unique identifier.

#### Args:
* generation_type (str): The type of resource to delete.
* uid (str): The unique identifier of the resource.

#### Returns:
* dict: A JSON response indicating the result of the deletion.

#### Example:
```python
from client import PixyClient

api_key = "your_api_key"
generation_type = "image"
uid = "desired_uid"

client = PixyClient(api_key)

response = client.delete(generation_type, uid)

print(response)

{
  "created_at": "2025-04-08T10:20:06.196Z",
  "updated_at": "2025-04-08T10:20:06.196Z",
  "is_deleted": False,
  "meta_data": {},
  "uid": "desired_uid",
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "task_status": "draft",
  "task_report": "string",
  "task_progress": -1,
  "task_logs": [],
  "task_references": {
    "tasks": [],
    "mode": "serial"
  },
  "task_start_at": "2025-04-08T10:20:06.196Z",
  "task_end_at": "2025-04-08T10:20:06.196Z",
  "webhook_url": "string",
  "engine": "flux_schnell",
  "aspect_ratio": "1:1",
  "delineation": "string",
  "context": [
    {}
  ],
  "enhance_prompt": False,
  "prompt": "string",
  "error": "string",
  "bulk": "string",
  "status": "init",
  "results": [
    {
      "url": "string",
      "width": 0,
      "height": 0
    }
  ],
  "usage_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### ```PixyClient.update(generation_type: str, uid: str, properties: dict) -> dict```

#### Description:
Retrieves a resource by its unique identifier.

#### Args:
* generation_type (str): The type of resource to retrieve.
* uid (str): The unique identifier of the resource.
* properties (dict): Set of the properties to be updated, in the form of key-value pairs.

#### Returns:
* dict: A JSON response inclding the desired resource.

#### Example:

```python
from client import PixyClient

api_key = "your_api_key"
client = PixyClient(api_key)

generation_type = "image"
uid = "desired_uid"
properties = {"delineation": "a blue kite flying over a green valley"}

response = client.update(generation_type, uid, properties)

print(response)

>>>{
>>>  "created_at": "2025-04-08T09:08:45.129Z",
>>>  "updated_at": "2025-04-08T09:08:45.129Z",
>>>  "is_deleted": false,
>>>  "meta_data": {},
>>>  "uid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
>>>  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
>>>  "task_status": "draft",
>>>  "task_report": "string",
>>>  "task_progress": -1,
>>>  "task_logs": [],
>>>  "task_references": {
>>>    "tasks": [],
>>>    "mode": "serial"
>>>  },
>>>  "task_start_at": "2025-04-08T09:08:45.129Z",
>>>  "task_end_at": "2025-04-08T09:08:45.129Z",
>>>  "webhook_url": "string",
>>>  "engine": "photon_flash",
>>>  "aspect_ratio": "1:1",
>>>  "delineation": "a blue kite flying over a green valley",
>>>  "context": [
>>>    {}
>>>  ],
>>>  "enhance_prompt": True,
>>>  "prompt": "string",
>>>  "error": "string",
>>>  "bulk": "string",
>>>  "status": "init",
>>>  "results": [
>>>    {
>>>      "url": "string",
>>>      "width": 0,
>>>      "height": 0
>>>    }
>>>  ],
>>>  "usage_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
>>>}
```