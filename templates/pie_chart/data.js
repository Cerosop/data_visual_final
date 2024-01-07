let res = JSON.parse(document.getElementById('res').innerHTML);
let continent_people_2011 = [];

for (var k1 in res) {
    for (var k2 in res[k1]) {
        for (var y in res[k1][k2]) {
            for (a in res[k1][k2][y]) {
                if (k1 == "continent" && k2 == "people" && y == 2011) {
                    let newEvaluation = {
                        "name": res[k1][k2][y][a][0],
                        "count": res[k1][k2][y][a][1]
                    };
                    continent_people_2011.push(newEvaluation);
                }

            }
        }
    }
}
