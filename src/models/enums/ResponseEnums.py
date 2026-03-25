from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATION_SUCCESS = "file validation successful"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDED = "file size exceeded"   
    FILE_UPLOAD_SUCCESS = "file upload successful"
    FILE_UPLOAD_FAILED = "file upload failed"
    PROCESSING_SUCCESS = "processing successful"
    PROCESSING_FAILED = "processing failed"
    NO_FILES_ERROR = "not_found_files"
    FILE_ID_ERROR = "no_file_found_with_this_id"
    
