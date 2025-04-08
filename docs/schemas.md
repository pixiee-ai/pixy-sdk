# Schemas API Reference

To avoid data validation issues, we define custom data classes for the schemas; in this section, we go through each of them individually.

## ```ImageGenProperties```

### Description:
Represents the properties for generating an image.

### Attributes:
* engine<span style="color:red">*</span> (str): The engine to use for generating the image; currently supported options are: "flux_schnell", "flux_1.1", "flux_pro", "imagen", "photon_flash", "photon", "dalle", "ideogram_turbo", "ideogram", "midjourney" and "stability".
* aspect_ratio (str | None ): The desired aspect ratio; make sure that the desired aspect ratio is supported by the selected engine; JSON object below summarizes the supported aspect ratio for each engine. The default value is "1:1".

```json
{
    "flux_schnell": ["4:5", "9:16", "3:2", "1:1", "21:9", "16:9", "9:21", "4:3", "3:4", "2:3", "5:4"],
	"flux_1.1": ["4:5", "9:16", "3:2", "1:1", "21:9", "16:9", "9:21", "4:3", "3:4", "2:3", "5:4"],
	"flux_pro": ["4:5", "9:16", "3:2", "1:1", "16:9", "4:3", "3:4", "2:3", "5:4"],
	"imagen": ["9:16", "1:1", "16:9", "4:3", "3:4"],
	"photon_flash": ["9:16", "1:1", "21:9", "9:21", "16:9", "4:3", "3:4"],
	"photon": ["9:16", "1:1", "21:9", "9:21", "16:9", "4:3", "3:4"],
	"dalle": ["1:1", "4:7", "7:4"],
	"ideogram_turbo": ["9:16", "3:2", "16:10", "1:1", "16:9", "3:1", "10:16", "4:3", "3:4", "2:3", "1:3"],
	"ideogram": ["9:16", "3:2", "16:10", "1:1", "16:9", "3:1", "10:16", "4:3", "3:4", "2:3", "1:3"],
	"midjourney": ["4:5", "9:16", "1:3", "3:2", "16:10", "1:1", "7:4", "4:7", "9:21", "16:9", "21:9", "3:1", "10:16", "4:3", "3:4", "2:3", "5:4"],
	"stability": ["4:5", "9:16", "3:2", "1:1", "21:9", "16:9", "9:21", "4:3", "3:4", "2:3", "5:4"],
}
```

* delineation<span style="color:red">*</span> (str): The textual prompt for image generation.
* context (List [dict] | None): <span style="color:red">The context for image generation.</span>
* enhance_prompt (bool | None): Whether to enhance the prompt with an automated assitance or not.

### Example:

```python
from core.schemas import ImageGenProperties

properties = ImageGenProperties(
    engine = "photon_flash",
    aspect_ratio = "1:1",
    delineation = "a red kite flying over the sea",
    context = [{}],
    enhance_prompt = True
)
```

## ```SubtitleGenProperties```

### Description:
Represents the properties for generating subtitles.

### Attributes:
* url<span style="color:red">*</span> (str): The downloadable link of the video or audio file.
* source_language (str): The original language that the desired media is in; currently supported languages are: "English", "Persian", "Arabic", "Turkish", "French", "Spanish", "German", "Italian", "Portuguese", "Dutch", "Russian", "Polish", "Romanian", "Bulgarian", "Hungarian", "Czech", "Greek", "Hebrew", "Japanese", "Korean", "Mandarin", "Vietnamese" and "Indonesian". Pass ```None``` or "auto" for automatic source language detection.
* target_language (str): The desired language for the subtitle; valid choices are the same as `source_language`. Default value is "Persian".
* diarization (bool): The generated subtitle can be labeled by speakers or not; default value is False.
* enhanced (bool): The generated subtitle can be enhanced (for higher quality)or not; default value is True.
* <span style="color:red">meta_data: dict | None = None</span>
* <span style="color:red">webhook_url: str| None = None</span>

### Example:

```python
from core.schemas import SubtitleGenProperties

props = SubtitleGenProperties(
    url="https://example.com/video.mp4",
    source_language="English",
    target_language="French",
    diarization=True,
    enhanced=False,
    meta_data=meta,
    webhook_url="https://example.com/webhook"
)
```

## ```VideoGenProperties```

### Description:
Represents the properties for generating videos.

### Attributes:
* user_prompt (str)<span style="color:red">*</span>: The textual prompt for video generation. 
* image_url (str | None): The downloadable link of the reference image file; declare this only for models that support image-to-video generation. For models that only support text-to-video generation, pass ```None```. Checkout the JSON object below to see which models support image-to-video generation.

```json
{
	"hailou": {"text_to_video": True, "image_to_video": True,},
	"kling": {"text_to_video": True, "image_to_video": True,},
	"hunyuanimageto": {"text_to_video": True, "image_to_video": True,},
	"runway": {"text_to_video": True, "image_to_video": True,},
	"minimax": {"text_to_video": True, "image_to_video": True,},
	"hailoutext": {"text_to_video": True, "image_to_video": False,},
	"klingtext": {"text_to_video": True, "image_to_video": False,},
	"klingprotext": {"text_to_video": True, "image_to_video": False,},
	"klingpro": {"text_to_video": True, "image_to_video": False,},
	"hunyuan": {"text_to_video": True, "image_to_video": False,},
	"luma": {"text_to_video": True, "image_to_video": False,},
  }
```

* <span style="color:red">meta_data (dict | None):</span>
* engine (VideoGenEngines)<span style="color:red">*</span>: The engine to use for generating the image; currently supported options are: "hailou", "kling", "hunyuanimageto", "runway", "minimax", "hailoutext", "klingtext", "klingprotext", "klingpro", "hunyuan", "luma".
* <span style="color:red">webhook_url (str | None): = None</span>

### Example:

```python
from core.schemas import VideoGenProperties

properties = ImageGenProperties(
    user_prompt = "a red kite flying over the sea",
    image_url = "https://example.com/image.jpg",
    meta_data = {},
    engine = "hailou",
    webhook_url = "https://example.com/webhook"
)
```

## ```GetListParameters```

### Description:
Represents the parameters for retrieving a list of resources.

### Attributes:
* offset (int): The offset for pagination.
* limit (int): The maximum number of resources to retrieve.
* created_at_from (str | None): The start date for filtering by creation date.
* created_at_to (str | None): The end date for filtering by creation date.

### Example:

```python
from core.schemas import GetListParameters

params = GetListParameters(
    offset = 0,
    limit = 2,
    created_at_from = "2025-02-01T00:00:00.000000",
    created_at_to = "2025-05-01T00:00:00.000000",
)
```