let myGraph3 = document.getElementById('myGraph3');

let trace1 ={
  type :"pie",
  labels :[],
  values :[],
  domain :{
    row:0,
    column:0,  
  },
  showlegend: true, 
  name: 'Dataset 1',
  marker: {
    colors: ['#EB773B', '#E6B049', '#E68B29', '#E5AD82', '#FBC15E', '#8EBA42', '#FFB5B8']
  }
};

for (let x = 0; x < evaluation_ratio_1.length; x++) {
  trace1.labels[x] = evaluation_ratio_1[x]["name"]; 
  trace1.values[x] = evaluation_ratio_1[x]["count"];
}

let data3 = [trace1];

let layout3 = {
    margin: {
        t: 50, 
        l: 10
    },
    grid: {
        rows: 1,
        columns: 1
    },
    title: "台灣原住民語分布比較"
};

Plotly.newPlot(myGraph3, data3, layout3);
