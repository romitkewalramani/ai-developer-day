from typing import Optional, List
from pydantic import BaseModel, Field, field_validator


class Movie(BaseModel):
    """Base movie model with all fields."""
    id: int = Field(..., description="Unique identifier for the movie", example=1)
    title: str = Field(..., description="Title of the movie", example="The Lion King", min_length=1)
    director: str = Field(..., description="Director of the movie", example="Roger Allers", min_length=1)
    release_year: int = Field(..., description="Year the movie was released", example=1994, ge=1900, le=2100)
    actors: Optional[List[str]] = Field(default=None, description="List of actor names", example=["Matthew Broderick", "Jeremy Irons"])
    genres: Optional[List[str]] = Field(default=None, description="List of genre categories", example=["Animation", "Adventure"])
    tags: Optional[List[str]] = Field(default=None, description="List of relevant keywords for the movie", example=["coming-of-age", "musical"])

    @field_validator('actors', 'genres', 'tags', mode='before')
    @classmethod
    def validate_array_items(cls, v):
        """Ensure all array items are non-empty strings."""
        if v is None:
            return v
        if isinstance(v, list):
            filtered = [item for item in v if item and isinstance(item, str) and item.strip()]
            return filtered if filtered else None
        return v


class MovieCreate(BaseModel):
    """Model for creating a new movie (without id field)."""
    title: str = Field(..., description="Title of the movie", example="Frozen", min_length=1)
    director: str = Field(..., description="Director of the movie", example="Chris Buck", min_length=1)
    release_year: int = Field(..., description="Year the movie was released", example=2013, ge=1900, le=2100)
    actors: Optional[List[str]] = Field(default=None, description="List of actor names", example=["Kristen Bell", "Idina Menzel"])
    genres: Optional[List[str]] = Field(default=None, description="List of genre categories", example=["Animation", "Musical"])
    tags: Optional[List[str]] = Field(default=None, description="List of relevant keywords for the movie", example=["sisterhood", "magic"])

    @field_validator('actors', 'genres', 'tags', mode='before')
    @classmethod
    def validate_array_items(cls, v):
        """Ensure all array items are non-empty strings."""
        if v is None:
            return v
        if isinstance(v, list):
            filtered = [item for item in v if item and isinstance(item, str) and item.strip()]
            return filtered if filtered else None
        return v


class MovieUpdate(BaseModel):
    """Model for updating a movie (all fields optional)."""
    title: Optional[str] = Field(default=None, description="Title of the movie", example="The Lion King", min_length=1)
    director: Optional[str] = Field(default=None, description="Director of the movie", example="Roger Allers", min_length=1)
    release_year: Optional[int] = Field(default=None, description="Year the movie was released", example=1994, ge=1900, le=2100)
    actors: Optional[List[str]] = Field(default=None, description="List of actor names", example=["Matthew Broderick", "Jeremy Irons"])
    genres: Optional[List[str]] = Field(default=None, description="List of genre categories", example=["Animation", "Adventure"])
    tags: Optional[List[str]] = Field(default=None, description="List of relevant keywords for the movie", example=["coming-of-age", "musical"])

    @field_validator('actors', 'genres', 'tags', mode='before')
    @classmethod
    def validate_array_items(cls, v):
        """Ensure all array items are non-empty strings."""
        if v is None:
            return v
        if isinstance(v, list):
            filtered = [item for item in v if item and isinstance(item, str) and item.strip()]
            return filtered if filtered else None
        return v


class MovieResponse(BaseModel):
    """Model for movie response (with id included)."""
    id: int = Field(..., description="Unique identifier for the movie", example=1)
    title: str = Field(..., description="Title of the movie", example="The Lion King", min_length=1)
    director: str = Field(..., description="Director of the movie", example="Roger Allers", min_length=1)
    release_year: int = Field(..., description="Year the movie was released", example=1994, ge=1900, le=2100)
    actors: Optional[List[str]] = Field(default=None, description="List of actor names", example=["Matthew Broderick", "Jeremy Irons"])
    genres: Optional[List[str]] = Field(default=None, description="List of genre categories", example=["Animation", "Adventure"])
    tags: Optional[List[str]] = Field(default=None, description="List of relevant keywords for the movie", example=["coming-of-age", "musical"])


class DeleteResponse(BaseModel):
    """Model for delete operation response."""
    message: str = Field(..., description="Success message", example="Movie deleted successfully")

