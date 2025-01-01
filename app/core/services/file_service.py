
from app.core.models.base_entity import BaseEntity
from app.core.repositories.base_repository import BaseRepository

class FileUploadService:
    """
    Service to handle operations related to file uploads.
    """
    SUPPORTED_FILE_TYPES = {"pdf", "docx", "txt"}  # Avoid magic numbers or strings

    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def upload_file(self, file_path: str, file_extension: str, uploader_id: int) -> BaseEntity:
        """
        Validates file type and uploads the file.
        """
        if file_extension.lower() not in self.SUPPORTED_FILE_TYPES:
            raise ValueError(f"Unsupported file type: {file_extension}. Supported types are: {', '.join(self.SUPPORTED_FILE_TYPES)}.")
        return await self.repository.create_record(file_path=file_path, file_type=file_extension, uploaded_by=uploader_id)
