from .schemas import ImageGenProperties, VideoGenProperties, SubtitleGenProperties


class _Settings:

    url_mapping = {
        "api_key_verification": "https://sso.pixy.ir/api_key/verify",
        "image": "https://media.pixy.ir/v1/apps/imagine/imagination/",
        "video": "https://media.pixy.ir/v1/apps/videogen/videos/",
        "subtitle": "https://media.pixy.ir/v1/apps/subtitle/subtitles/",
    }

    properties_mapping = {
        "image": ImageGenProperties,
        "video": VideoGenProperties,
        "subtitle": SubtitleGenProperties,
    }


class Settings:
    def __init__(
        self,
        url_mapping: dict = {
            "api_key_verification": "https://sso.pixy.ir/api_key/verify",
            "image": "https://media.pixy.ir/v1/apps/imagine/imagination/",
            "video": "https://media.pixy.ir/v1/apps/videogen/videos/",
            "subtitle": "https://media.pixy.ir/v1/apps/subtitle/subtitles/",
        },
        properties_mapping: dict = {
            "image": ImageGenProperties,
            "video": VideoGenProperties,
            "subtitle": SubtitleGenProperties,
        },
    ):
        self.url_mapping = url_mapping
        self.properties_mapping = properties_mapping
