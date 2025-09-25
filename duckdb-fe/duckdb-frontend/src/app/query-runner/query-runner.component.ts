import { Component } from '@angular/core';
import { QueryService } from '../query.service';


@Component({
  selector: 'app-query-runner',
  templateUrl: './query-runner.component.html',
  styleUrls: ['./query-runner.component.css']
})
export class QueryRunnerComponent {
  sqlQuery: string = '';
  result: any = null;
  error: string = '';

  constructor(private queryService: QueryService) {}

  executeQuery() {
    this.queryService.runQuery(this.sqlQuery).subscribe({
      next: res => {
        this.result = res;
        this.error = '';
      },
      error: err => {
        this.error = err.message || 'Error executing query';
        this.result = null;
      }
    });
  }
}