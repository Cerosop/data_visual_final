let evaluation_ratio_1 = [
    {
        "name": "平時",
        "count": 10
    },
    {
        "name": "出席",
        "count": 20
    },
    {
        "name": "期中評量",
        "count": 30
    },
    {
        "name": "期末評量",
        "count": 40
    },
];
let evaluation_ratio_2 = [
    {
        "name": "平時",
        "count": 20
    },
    {
        "name": "出席",
        "count": 10
    },
    {
        "name": "期中評量",
        "count": 35
    },
    {
        "name": "期末評量",
        "count": 35
    },
];
let evaluation_ratio_3 = [
    {
        "name": "平時",
        "count": 10
    },
    {
        "name": "出席",
        "count": 30
    },
    {
        "name": "期中評量",
        "count": 20
    },
    {
        "name": "期末評量",
        "count": 40
    },
];
let evaluation_ratio_4 = [
    {
        "name": "平時",
        "count": 10
    },
    {
        "name": "出席",
        "count": 10
    },
    {
        "name": "期中評量",
        "count": 30
    },
    {
        "name": "期末評量",
        "count": 50
    },
];
// https://www.ey.gov.tw/state/6A206590076F7EF/8b5032af-1a67-4c02-bd16-8791aa459cd2

let continent_people_2011 = [];

for (let k1 in res) {
    for (let k2 in res[k1]) {
        for (let y in res[k1][k2]) {
            for (let a of res[k1][k2][y]) {
                if(k1 == "continent"){
                    if(k2 == "people"){
                        if(y == "y"){
                            let newEvaluation = {
                            "name": a[0],
                            "count": a[1]
                            };
                            continent_people_2011.push(newEvaluation);
                        }
                    }
                }
            }
        }
    }
}