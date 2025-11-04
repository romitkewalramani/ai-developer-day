import { Injectable } from '@nestjs/common';
import { promises as fs } from 'fs';
import { join } from 'path';
import { Movie } from '../movies/entities/movie.entity';

@Injectable()
export class StorageService {
  private readonly filePath = join(process.cwd(), 'movies.json');

  async readMovies(): Promise<Movie[]> {
    try {
      const data = await fs.readFile(this.filePath, 'utf-8');
      return JSON.parse(data);
    } catch (error) {
      // If file doesn't exist, create it with empty array
      if (error.code === 'ENOENT') {
        await this.writeMovies([]);
        return [];
      }
      throw error;
    }
  }

  async writeMovies(movies: Movie[]): Promise<void> {
    await fs.writeFile(this.filePath, JSON.stringify(movies, null, 2), 'utf-8');
  }
}

