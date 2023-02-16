import mimetypes
from typing import Dict
import os
from pydub.utils import mediainfo

from edenai_apis.utils.files import FileInfo, FileWrapper

feature_path = os.path.dirname(os.path.dirname(__file__))

data_path = os.path.join(feature_path, "data")

video_path = f"{data_path}/labels.mp4"

mime_type = mimetypes.guess_type(video_path)[0]
file_info= FileInfo(
    os.stat(video_path).st_size,
    mime_type,
    [extension[1:] for extension in mimetypes.guess_all_extensions(mime_type)],
    mediainfo(video_path).get("sample_rate", "44100"),
    mediainfo(video_path).get("channels", "1")
)
file_wrapper = FileWrapper(video_path, "", file_info)

def label_detection_arguments() -> Dict:
    return {"file": file_wrapper}
