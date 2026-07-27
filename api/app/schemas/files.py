from pydantic import BaseModel


class FileItem(BaseModel):

    name: str

    path: str

    size: int

    modified: str

    type: str



class FilesInfo(BaseModel):

    path: str

    status: str



class FilesList(BaseModel):

    status: str

    count: int

    files: list[FileItem]
