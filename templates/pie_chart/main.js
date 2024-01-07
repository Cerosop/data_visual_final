let myGraph = document.getElementById('myGraph');

let trace1 = {};
trace1.type = "pie";
trace1.title = "機器學習概論";
trace1.labels = [];
trace1.values = [];
trace1.hole = 0.5
trace1.domain = {
    row:0,
    column:0
};

for(let i=0;i<continent_people_2011.length;i++){
    trace1.labels[i] = continent_people_2011[i]['name'];
    trace1.values[i] = continent_people_2011[i]['count'];
}

let trace2 = {};
trace2.type = "pie";
trace2.title = "資料視覺化";
trace2.labels = [];
trace2.values = [];
trace2.hole = 0.5
trace2.domain = {
    row:0,
    column:1
};

for(let i=0;i<evaluation_ratio_2.length;i++){
    trace2.labels[i] = evaluation_ratio_2[i]['name'];
    trace2.values[i] = evaluation_ratio_2[i]['count'];
}

let trace3 = {};
trace3.type = "pie";
trace3.title = "人工智慧與永續發展";
trace3.labels = [];
trace3.values = [];
trace3.hole = 0.5
trace3.domain = {
    row:1,
    column:0
};

for(let i=0;i<evaluation_ratio_3.length;i++){
    trace3.labels[i] = evaluation_ratio_3[i]['name'];
    trace3.values[i] = evaluation_ratio_3[i]['count'];
}

let trace4 = {};
trace4.type = "pie";
trace4.title = "Python程式設計";
trace4.labels = [];
trace4.values = [];
trace4.hole = 0.5
trace4.domain = {
    row:1,
    column:1
};

for(let i=0;i<evaluation_ratio_4.length;i++){
    trace4.labels[i] = evaluation_ratio_4[i]['name'];
    trace4.values[i] = evaluation_ratio_4[i]['count'];
}


let data = [];
data.push(trace1);
data.push(trace2);
data.push(trace3);
data.push(trace4);

let layout = {
    margin:{
        t:50,
    },
    grid:{
        rows:2,
        columns:2
    },
    title:'Pie Chart'
};
Plotly.newPlot(myGraph, data, layout);