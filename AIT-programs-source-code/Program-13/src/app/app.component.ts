import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'HelloApp';
  show = true;
  show1 = false;
  msg = "h1";
  color1 = "blue";
  arr = ["SIMCA", "MCA", "MBA", "PHD"];
  Emp = [
    {
      Emp_id: 101,
      Emp_name: "SIMCA",
      Emp_sal: 12000
    },
    {
      Emp_id: 102,
      Emp_name: "SIOM",
      Emp_sal: 10000
    },
    {
      Emp_id: 103,
      Emp_name: "SIBAR",
      Emp_sal: 10000
    }
  ];
}
