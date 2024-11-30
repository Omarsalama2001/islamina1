from dataclasses import dataclass


@dataclass
class Radio:
    country_code: str
    title: str
    audio_url: str