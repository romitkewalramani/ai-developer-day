import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';
import {
  IsString,
  IsNotEmpty,
  IsNumber,
  IsOptional,
  IsArray,
  Min,
  Max,
} from 'class-validator';

export class CreateMovieDto {
  @ApiProperty({
    description: 'Title of the movie',
    example: 'The Lion King',
  })
  @IsString()
  @IsNotEmpty()
  title: string;

  @ApiProperty({
    description: 'Director of the movie',
    example: 'Roger Allers',
  })
  @IsString()
  @IsNotEmpty()
  director: string;

  @ApiProperty({
    description: 'Year the movie was released',
    example: 1994,
    minimum: 1900,
    maximum: 2100,
  })
  @IsNumber()
  @Min(1900)
  @Max(2100)
  releaseYear: number;

  @ApiPropertyOptional({
    description: 'List of actor names',
    example: ['Matthew Broderick', 'Jeremy Irons', 'James Earl Jones'],
    type: [String],
  })
  @IsOptional()
  @IsArray()
  @IsString({ each: true })
  actors?: string[];

  @ApiPropertyOptional({
    description: 'List of genre categories',
    example: ['Animation', 'Adventure', 'Drama'],
    type: [String],
  })
  @IsOptional()
  @IsArray()
  @IsString({ each: true })
  genres?: string[];

  @ApiPropertyOptional({
    description: 'List of relevant keywords for the movie',
    example: ['coming-of-age', 'musical', 'classic'],
    type: [String],
  })
  @IsOptional()
  @IsArray()
  @IsString({ each: true })
  tags?: string[];
}

