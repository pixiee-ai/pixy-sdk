# Utils API Reference

The Pixy SDK relys on a set of utility function, covering a wide range of tasks. In this section, each of them is discussed individually.

## ```verify(api_key: str) -> bool```

### Description:
Verifies the given API key.

### Args:
* api_key (str): The API key to verify.

### Returns:
* bool: True if the API key is valid, False otherwise.

### Example:
```python
from core.utils import verify

api_key = "your_api_key"
is_valid = verify(api_key)
print(is_valid)

>>> True
```

## ```generate(generation_type: str, properties: ImageGenProperties | VideoGenProperties | SubtitleGenProperties api_key: str,) -> dict```

### Description:
Generates a resource (image, video, subtitle) based on the given properties.

### Args:
* generation_type (str): The type of resource to generate; current valid choices are "image", "video" and "subtitle".
* properties (ImageGenProperties | VideoGenProperties | SubtitleGenProperties): The properties of the resource to generate; current valid choices are ImageGenProperties, VideoGenProperties and SubtitleGenProperties that correspond to "image", "video" and "subtitle", respectively.
* api_key (str): The API key to use for the request.

### Returns:
* dict: A JSON response containing the generated resource.

### Example:
```python
from core.utils import generate
from core.schemas import ImageGenProperties

api_key = "your_api_key"
generation_type = "image"
properties = ImageGenProperties(
    engine = "photon_flash",
    aspect_ratio = "1:1",
    delination = "a red kite flying over the sea",
    context = [{}],
    enhance_prompt = True
)
resource = generate(generation_type, properties, api_key)
print(resource)

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

## ```get_by_uid(generation_type: str, uid: str, api_key: str) -> dict```

### Description:
Retrieves a resource by its unique identifier (UID).

### Args:
* generation_type (str): The type of resource to retrieve; current valid choices are "image", "video" and "subtitle".
* uid (str): The desired UID.
* api_key (str): The API key to use for the request.

### Returns:
* dict: A JSON response inclding the desired resource.

### Example:

```python
from core.utils import get_by_uid

api_key = "your_api_key"
generation_type = "image"
uid = "desired_UID"

resource = get_by_uid(generation_type, uid, api_key)

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

## ```get_list(generation_type: str, params: GetListParameters | None, api_key: str) -> dict```

### Description:
Retrieves a list of resources filtered by the given parameters.

### Args:
* generation_type (str): The type of resource to retrieve.
* params (GetListParameters | None): The parameters to filter the results by.
* api_key (str): The API key to use for the request.

### Returns:
* dict: A JSON response containing the retrieved resources.

### Example:

```python
from core.schemas import GetListParameters
from core.utils import get_list

api_key = "your_api_key"
generation_type = "image"

params = GetListParameters(
    offset = 0,
    limit = 2,
    created_at_from = "2025-02-01T00:00:00.000000",
    created_at_to = "2025-05-01T00:00:00.000000",
)

resources = get_list(
    generation_type,
    params,
    api_key
)
print(lenresources)

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

## ```delete(generation_type: str, uid: str, api_key: str) -> dict```

### Description:
Deletes a resource by its unique identifier.

### Args:
* generation_type (str): The type of resource to delete.
* uid (str): The unique identifier of the resource.
* api_key (str): The API key to use for the request.

### Returns:
* dict: A JSON response indicating the result of the deletion.

### Example:

```python
from core.utils import delete

api_key = "your_api_key"
generation_type = "image"
uid = "desired_uid"

response = delete(generation_type, uid, api_key)

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

## ```update(generation_type: str, uid: str, properties: dict, api_key: str) -> dict```
    
### Description:
Updates a resource by its unique identifier with the given properties.

### Args:
* generation_type (str): The type of resource to update.
* uid (str): The unique identifier of the resource.
* properties (dict): The properties to update the resource with. This is supposed to only include the key-values to update.
* api_key (str): The API key to use for the request.

### Returns:
* dict: A JSON response containing the updated resource.

### Example:
```python
from core.utils import update

api_key = "your_api_key"
generation_type = "image"
uid = "desired_uid"
properties = {"delination": "a blue kite flying over a green valley"}

response = update(generation_type, uid, properties, api_key)

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