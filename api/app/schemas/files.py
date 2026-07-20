from pydantic import BaseModel


class FilesInfo(BaseModel):

    path: str
    status: str



class FilesList(BaseModel):

    status: str
    count: int
    files: list[str]
