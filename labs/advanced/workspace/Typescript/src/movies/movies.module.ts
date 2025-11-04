import { Module } from '@nestjs/common';
import { MoviesController } from './movies.controller';
import { MoviesService } from './movies.service';
import { StorageService } from '../storage/storage.service';

@Module({
  controllers: [MoviesController],
  providers: [MoviesService, StorageService],
})
export class MoviesModule {}

