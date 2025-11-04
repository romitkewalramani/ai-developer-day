import {
  Injectable,
  NotFoundException,
} from '@nestjs/common';
import { StorageService } from '../storage/storage.service';
import { Movie } from './entities/movie.entity';
import { CreateMovieDto } from './dto/create-movie.dto';
import { UpdateMovieDto } from './dto/update-movie.dto';

@Injectable()
export class MoviesService {
  constructor(private readonly storageService: StorageService) {}

  async findByTitle(movieName: string): Promise<Movie[]> {
    const movies = await this.storageService.readMovies();
    return movies.filter((movie) => movie.title === movieName);
  }

  async create(createMovieDto: CreateMovieDto): Promise<Movie> {
    const movies = await this.storageService.readMovies();

    // Generate next available ID
    const nextId =
      movies.length > 0 ? Math.max(...movies.map((m) => m.id)) + 1 : 1;

    const newMovie: Movie = {
      id: nextId,
      ...createMovieDto,
    };

    movies.push(newMovie);
    await this.storageService.writeMovies(movies);

    return newMovie;
  }

  async update(id: number, updateMovieDto: UpdateMovieDto): Promise<Movie> {
    const movies = await this.storageService.readMovies();
    const movieIndex = movies.findIndex((movie) => movie.id === id);

    if (movieIndex === -1) {
      throw new NotFoundException(`Movie with ID ${id} not found`);
    }

    // Update only provided fields
    const updatedMovie: Movie = {
      ...movies[movieIndex],
      ...updateMovieDto,
      id, // Ensure ID remains unchanged
    };

    movies[movieIndex] = updatedMovie;
    await this.storageService.writeMovies(movies);

    return updatedMovie;
  }

  async remove(id: number): Promise<void> {
    const movies = await this.storageService.readMovies();
    const movieIndex = movies.findIndex((movie) => movie.id === id);

    if (movieIndex === -1) {
      throw new NotFoundException(`Movie with ID ${id} not found`);
    }

    movies.splice(movieIndex, 1);
    await this.storageService.writeMovies(movies);
  }
}

