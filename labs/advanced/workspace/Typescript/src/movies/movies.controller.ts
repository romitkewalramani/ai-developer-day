import {
  Controller,
  Get,
  Post,
  Patch,
  Delete,
  Body,
  Param,
  Query,
  HttpCode,
  HttpStatus,
  BadRequestException,
} from '@nestjs/common';
import {
  ApiTags,
  ApiOperation,
  ApiResponse,
  ApiQuery,
  ApiParam,
  ApiBody,
} from '@nestjs/swagger';
import { MoviesService } from './movies.service';
import { Movie } from './entities/movie.entity';
import { CreateMovieDto } from './dto/create-movie.dto';
import { UpdateMovieDto } from './dto/update-movie.dto';

@ApiTags('Movies')
@Controller('movies')
export class MoviesController {
  constructor(private readonly moviesService: MoviesService) {}

  @Get()
  @ApiOperation({
    summary: 'Get movie by name',
    description: 'Search for movies by exact case-sensitive title match',
  })
  @ApiQuery({
    name: 'movie_name',
    required: true,
    description: 'Exact case-sensitive movie title to search for',
    type: String,
    example: 'The Lion King',
  })
  @ApiResponse({
    status: 200,
    description: 'Array of matching movies (can be empty)',
    type: [Movie],
  })
  async findByTitle(@Query('movie_name') movieName: string): Promise<Movie[]> {
    return this.moviesService.findByTitle(movieName);
  }

  @Post()
  @ApiOperation({
    summary: 'Create a new movie',
    description: 'Create a new movie with auto-generated ID',
  })
  @ApiBody({
    type: CreateMovieDto,
    description: 'Movie data to create (ID is auto-assigned)',
  })
  @ApiResponse({
    status: 201,
    description: 'Movie created successfully',
    type: Movie,
  })
  @ApiResponse({
    status: 400,
    description: 'Validation failed (missing required fields, invalid data types)',
  })
  @HttpCode(HttpStatus.CREATED)
  async create(@Body() createMovieDto: CreateMovieDto): Promise<Movie> {
    return this.moviesService.create(createMovieDto);
  }

  @Patch(':id')
  @ApiOperation({
    summary: 'Update a movie',
    description: 'Partially update a movie by ID (only provided fields are updated)',
  })
  @ApiParam({
    name: 'id',
    description: 'Unique identifier of the movie to update',
    type: Number,
    example: 1,
  })
  @ApiBody({
    type: UpdateMovieDto,
    description: 'Partial movie data to update',
  })
  @ApiResponse({
    status: 200,
    description: 'Movie updated successfully',
    type: Movie,
  })
  @ApiResponse({
    status: 404,
    description: 'Movie with given ID not found',
  })
  @ApiResponse({
    status: 400,
    description: 'Validation failed for provided fields',
  })
  async update(
    @Param('id') id: string,
    @Body() updateMovieDto: UpdateMovieDto,
  ): Promise<Movie> {
    const movieId = parseInt(id, 10);
    if (isNaN(movieId)) {
      throw new BadRequestException('Invalid ID format');
    }
    return this.moviesService.update(movieId, updateMovieDto);
  }

  @Delete(':id')
  @ApiOperation({
    summary: 'Delete a movie',
    description: 'Delete a movie by ID',
  })
  @ApiParam({
    name: 'id',
    description: 'Unique identifier of the movie to delete',
    type: Number,
    example: 1,
  })
  @ApiResponse({
    status: 200,
    description: 'Movie deleted successfully',
    schema: {
      type: 'object',
      properties: {
        message: {
          type: 'string',
          example: 'Movie deleted successfully',
        },
      },
    },
  })
  @ApiResponse({
    status: 404,
    description: 'Movie with given ID not found',
  })
  async remove(@Param('id') id: string): Promise<{ message: string }> {
    const movieId = parseInt(id, 10);
    if (isNaN(movieId)) {
      throw new BadRequestException('Invalid ID format');
    }
    await this.moviesService.remove(movieId);
    return { message: 'Movie deleted successfully' };
  }
}

