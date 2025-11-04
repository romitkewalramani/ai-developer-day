import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';

export class Movie {
  @ApiProperty({
    description: 'Unique identifier for the movie',
    example: 1,
  })
  id: number;

  @ApiProperty({
    description: 'Title of the movie',
    example: 'The Lion King',
  })
  title: string;

  @ApiProperty({
    description: 'Director of the movie',
    example: 'Roger Allers',
  })
  director: string;

  @ApiProperty({
    description: 'Year the movie was released',
    example: 1994,
    minimum: 1900,
    maximum: 2100,
  })
  releaseYear: number;

  @ApiPropertyOptional({
    description: 'List of actor names',
    example: ['Matthew Broderick', 'Jeremy Irons', 'James Earl Jones'],
    type: [String],
  })
  actors?: string[];

  @ApiPropertyOptional({
    description: 'List of genre categories',
    example: ['Animation', 'Adventure', 'Drama'],
    type: [String],
  })
  genres?: string[];

  @ApiPropertyOptional({
    description: 'List of relevant keywords for the movie',
    example: ['coming-of-age', 'musical', 'classic'],
    type: [String],
  })
  tags?: string[];
}

