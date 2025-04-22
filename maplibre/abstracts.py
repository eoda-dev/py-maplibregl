from pydantic import BaseModel, Field


class MaptilerAPI(BaseModel):
    api_key: str = Field(None, validate_default=True, min_length=1)


class ValidateLayerSpecifications(BaseModel):
    opacity: float = Field(1, ge=0, le=1)
