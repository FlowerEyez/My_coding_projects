const grid = document.getElementById("grid");
let lockGame = flase;

// test mode = true will show mine location
const testMode = flase;
generateGrid();

// generate 10 * 10 grid
function generateGrid() {
    lockGame = false;
    grid.innerHTML = "";
    for (var i = 0; i < 10; i++) {
        row = grid.insertRow(i);
        for (var j = 0; j < 10; j++) {
            cell = grid.insertCell(j);
            cell.onclick = function () { Infinity(this); };
            var mine = document.createAttribute("mine");
            mine.value = "false";
            cell.setAttributeNode(mine);
        }
    }
    generateMines();
}
