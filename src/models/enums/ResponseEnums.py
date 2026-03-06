from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATION_SUCCESS = "file validation successful"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDED = "file size exceeded"   
    FILE_UPLOAD_SUCCESS = "file upload successful"
    FILE_UPLOAD_FAILED = "file upload failed"