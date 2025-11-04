from typing import List
from fastapi import APIRouter, HTTPException, Query, Path
from models import MovieCreate, MovieUpdate, MovieResponse, DeleteResponse
from storage import (
    read_movies,
    write_movies,
    get_next_id,
    find_movie_by_id,
    find_movies_by_title
)

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get(
    "",
    response_model=List[MovieResponse],
    summary="Get movies by name",
    description="Search for movies by exact case-sensitive title match. Returns all matching movies."
)
def get_movies(
    movie_name: str = Query(..., description="Exact case-sensitive movie title to search for", example="The Lion King")
) -> List[MovieResponse]:
    """
    Get movies by exact case-sensitive title match.
    
    - **movie_name**: Exact case-sensitive movie title to search for
    - Returns array of matching movies (empty array if no matches found)
    """
    movies = read_movies()
    matching_movies = find_movies_by_title(movies, movie_name)
    return [MovieResponse(**movie) for movie in matching_movies]


@router.post(
    "",
    response_model=MovieResponse,
    status_code=201,
    summary="Create a new movie",
    description="Create a new movie with auto-assigned ID. All required fields must be provided."
)
def create_movie(movie_data: MovieCreate) -> MovieResponse:
    """
    Create a new movie.
    
    - **title**: Movie title (required)
    - **director**: Director name (required)
    - **release_year**: Release year (required, 1900-2100)
    - **actors**: Optional list of actor names
    - **genres**: Optional list of genres
    - **tags**: Optional list of tags
    
    Returns the created movie with assigned ID.
    """
    movies = read_movies()
    next_id = get_next_id(movies)
    
    new_movie = {
        "id": next_id,
        "title": movie_data.title,
        "director": movie_data.director,
        "release_year": movie_data.release_year,
        "actors": movie_data.actors,
        "genres": movie_data.genres,
        "tags": movie_data.tags
    }
    
    movies.append(new_movie)
    write_movies(movies)
    
    return MovieResponse(**new_movie)


@router.patch(
    "/{id}",
    response_model=MovieResponse,
    summary="Update a movie",
    description="Partially update a movie by ID. Only provided fields will be updated."
)
def update_movie(
    id: int = Path(..., description="Unique identifier of the movie to update", example=1),
    movie_data: MovieUpdate = ...
) -> MovieResponse:
    """
    Update a movie by ID.
    
    - **id**: Movie ID to update
    - **movie_data**: Fields to update (all optional)
    
    Returns the updated movie object.
    """
    movies = read_movies()
    movie = find_movie_by_id(movies, id)
    
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with id {id} not found")
    
    # Update only provided fields
    update_dict = movie_data.model_dump(exclude_unset=True)
    
    # Remove id from update dict if present (shouldn't be, but safety check)
    update_dict.pop('id', None)
    
    # Update movie
    movie.update(update_dict)
    
    # Find and update in list
    for i, m in enumerate(movies):
        if m.get('id') == id:
            movies[i] = movie
            break
    
    write_movies(movies)
    
    return MovieResponse(**movie)


@router.delete(
    "/{id}",
    response_model=DeleteResponse,
    summary="Delete a movie",
    description="Delete a movie by ID."
)
def delete_movie(
    id: int = Path(..., description="Unique identifier of the movie to delete", example=1)
) -> DeleteResponse:
    """
    Delete a movie by ID.
    
    - **id**: Movie ID to delete
    
    Returns success message.
    """
    movies = read_movies()
    movie = find_movie_by_id(movies, id)
    
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with id {id} not found")
    
    # Remove movie from list
    movies = [m for m in movies if m.get('id') != id]
    write_movies(movies)
    
    return DeleteResponse(message="Movie deleted successfully")

