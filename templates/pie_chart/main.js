let myGraph = document.getElementById('myGraph');

let trace1 = {};
trace1.type = "pie";
trace1.title = "機器學習概論";
trace1.labels = [];
trace1.values = [];
trace1.hole = 0.5
trace1.domain = {
    row: 0,
    column: 0
};

for (let i = 0; i < continent_people_2011.length; i++) {
    trace1.labels[i] = continent_people_2011[i]['name'];
    trace1.values[i] = continent_people_2011[i]['count'];
}

let data = [];
data.push(trace1);

let layout = {
    margin: {
        t: 50,
    },
    title: 'Pie Chart'
};
console.log(myGraph)
Plotly.newPlot(myGraph, data, layout);