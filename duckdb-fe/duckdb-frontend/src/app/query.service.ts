import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QueryService {
  private apiUrl = 'http://localhost:8000/query';

  constructor(private http: HttpClient) {}

  runQuery(sql: string): Observable<any> {
    return this.http.post<any>(this.apiUrl, { sql });
  }
}
