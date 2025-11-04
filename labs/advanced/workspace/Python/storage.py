import json
from typing import List, Dict, Optional, Any
from pathlib import Path


JSON_FILE_PATH = Path("movies.json")


def read_movies() -> List[Dict[str, Any]]:
    """
    Read all movies from the JSON file.
    Creates an empty file if it doesn't exist.
    
    Returns:
        List of movie dictionaries
    """
    if not JSON_FILE_PATH.exists():
        # Create empty file if it doesn't exist
        write_movies([])
        return []
    
    try:
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                # If file is corrupted, reset it
                write_movies([])
                return []
            return data
    except (json.JSONDecodeError, IOError) as e:
        # If file is corrupted or can't be read, create empty file
        write_movies([])
        return []


def write_movies(movies: List[Dict[str, Any]]) -> None:
    """
    Write movies to the JSON file atomically.
    
    Args:
        movies: List of movie dictionaries to write
    """
    # Use atomic write: write to temp file first, then rename
    temp_file = JSON_FILE_PATH.with_suffix('.tmp')
    try:
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(movies, f, indent=2, ensure_ascii=False)
        # Atomic rename
        temp_file.replace(JSON_FILE_PATH)
    except IOError as e:
        # If temp file exists, remove it
        if temp_file.exists():
            temp_file.unlink()
        raise


def get_next_id(movies: List[Dict[str, Any]]) -> int:
    """
    Get the next available ID by finding the highest existing ID.
    
    Args:
        movies: List of movie dictionaries
        
    Returns:
        Next available ID (1 if list is empty)
    """
    if not movies:
        return 1
    max_id = max(movie.get('id', 0) for movie in movies)
    return max_id + 1


def find_movie_by_id(movies: List[Dict[str, Any]], movie_id: int) -> Optional[Dict[str, Any]]:
    """
    Find a movie by its ID.
    
    Args:
        movies: List of movie dictionaries
        movie_id: ID to search for
        
    Returns:
        Movie dictionary if found, None otherwise
    """
    for movie in movies:
        if movie.get('id') == movie_id:
            return movie
    return None


def find_movies_by_title(movies: List[Dict[str, Any]], title: str) -> List[Dict[str, Any]]:
    """
    Find movies by exact case-sensitive title match.
    
    Args:
        movies: List of movie dictionaries
        title: Exact title to search for (case-sensitive)
        
    Returns:
        List of matching movie dictionaries
    """
    return [movie for movie in movies if movie.get('title') == title]

