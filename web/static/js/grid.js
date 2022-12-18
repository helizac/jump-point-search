current_res = 1

var height = 12;
var width = 24;

let gridArray = Array(12);

for (var i = 0; i < gridArray.length; i++) {
    gridArray[i] = new Array(24);
}

for (var i = 0; i < 12; i++) {
    for (var j = 0; j < 24; j++) {
        gridArray[i][j] = -1;
    }
}

gridArray[9][21] = -2;

let isBlankEditable, isBlockEditable = false;

function createGrid() {

    document.write("<table>");

    for (var y = 0; y < height; y++) {
        document.write("<tr>");
        for (var x = 0; x < width; x++) {
            if(y == 2 && x == 2){
                document.write("<td class = 'start' id = " + y + "-" + x + "></td>");
            }
            else if(gridArray[y][x] == -2){
                document.write("<td class = 'destination' id = " + y + "-" + x + "></td>");
            }
            else if(gridArray[y][x] == -1){
                document.write("<td class = 'blank' id = " + y + "-" + x + "></td>");
            }
            else if(gridArray[y][x] == -10){
                document.write("<td class = 'block' id = " + y + "-" + x + "></td>");
            }
            else if(gridArray[y][x] == -5){
                document.write("<td class = 'path' id = " + y + "-" + x + "></td>");
            }
        }
        document.write("</tr>");
    }

    document.write("</table>");

}

function addBlankListener(elem){

    function BlankMouseDown(event){
        if(elem.className == "blank"){
            if(!isBlankEditable && !isBlockEditable){
                isBlankEditable = true;
                isBlockEditable = false;
                elem.className = "block";
                gridArray[elem.getAttribute("id").split("-")[0]][elem.getAttribute("id").split("-")[1]] = -10;
            }
        }
    }

    function BlankMouseOver(event){
        if(elem.className == "blank"){
            if(isBlankEditable){
                elem.className = "block";
                gridArray[elem.getAttribute("id").split("-")[0]][elem.getAttribute("id").split("-")[1]] = -10;
            }
        }
    }

    function BlankMouseUp(event){
        if(isBlankEditable || isBlankEditable){
            isBlankEditable = false;
            isBlockEditable = false;
        }
    }

    elem.addEventListener("mousedown", BlankMouseDown, true);
    elem.addEventListener("mouseenter", BlankMouseOver, true);
    elem.addEventListener("mouseup", BlankMouseUp, true);
}

function addBlockListener(elem){

    function BlockMouseDown(event){
        if(elem.className == "block"){
            if(!isBlankEditable && !isBlockEditable){
                isBlankEditable = false;
                isBlockEditable = true;
                elem.className = "blank";
                gridArray[elem.getAttribute("id").split("-")[0]][elem.getAttribute("id").split("-")[1]] = -1;
            }
        }
    }

    function BlockMouseOver(event){
        if(elem.className == "block"){
            if(isBlockEditable){
                elem.className = "blank";
                isBlockChanged = true;
                gridArray[elem.getAttribute("id").split("-")[0]][elem.getAttribute("id").split("-")[1]] = -1;
            }
        }
    }

    function BlockMouseUp(event){
        if(isBlockEditable || isBlankEditable){
            isBlankEditable = false;
            isBlockEditable = false;
            console.log(gridArray);
        }
    }
    elem.addEventListener("mousedown", BlockMouseDown, true);
    elem.addEventListener("mouseenter", BlockMouseOver, true);
    elem.addEventListener("mouseup", BlockMouseUp, true);
}

function setGrid(){
    var blanks = document.getElementsByClassName("blank");
    for ( let i = 0; i < blanks.length; i++ ){
        addBlankListener(blanks[i]);
        addBlockListener(blanks[i]);
    }
}

function returnGridArray(){
    return gridArray;
}

function updateGrid(array){
    gridArray = array;
}