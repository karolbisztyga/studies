import { TestBed } from '@angular/core/testing';

import { BasketServiceService } from './basket-service.service';

describe('BasketServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: BasketServiceService = TestBed.get(BasketServiceService);
    expect(service).toBeTruthy();
  });
});
