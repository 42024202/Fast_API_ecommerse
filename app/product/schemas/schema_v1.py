from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    """Base class for product."""
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    """Class for creating product."""
    pass

class ProductOut(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    """Class for output product."""
    id: int
