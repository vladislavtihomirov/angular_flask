import { Component, ViewChild, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'user-stats';
  items: any;
  page = 1;
  wordInput;

  constructor(private http: HttpClient) { }

  ngOnInit(){
    this.getUsers();
  }

  public search(){
    this.http.post('http://localhost:8050/search?word='+this.wordInput, 'test').subscribe(data => this.items = data);
  }

  public getUsers() {
    this.http.post('http://localhost:8050/users?page='+this.page, 'test').subscribe(data => this.items = data);
  }
}
