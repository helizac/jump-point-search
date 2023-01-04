current_res = 1

var height = 14;
var width = 26;

let gridArray = Array(height);

for (var i = 0; i < gridArray.length; i++) {
    gridArray[i] = new Array(width);
}

for (var i = 0; i < height; i++) {
    for (var j = 0; j < width; j++) {
        if((i === 0) || (j === 0) || (i === height-1) || (j === width-1)){
            gridArray[i][j] = -8
        }
        else{
            gridArray[i][j] = -7;
        }
    }
}

gridArray[3][3] = -1
gridArray[10][22] = -2;

console.log(gridArray);

let isBlankEditable, isBlockEditable = false;

function createGrid() {

    document.write("<table>");

    for (var y = 1; y < height-1; y++) {
        document.write("<tr>");
        for (var x = 1; x < width-1; x++) {
            console.log(gridArray[y][x]);
            if(gridArray[y][x] == -1){
                document.write("<td class = 'start' id = " + y + "-" + x + "></td>");
            }
            else if(gridArray[y][x] == -2){
                document.write("<td class = 'end' id = " + y + "-" + x + "></td>");
            }
            else if(gridArray[y][x] == -7){
                document.write("<td class = 'blank' id = " + y + "-" + x + "></td>");
            }
            else if(gridArray[y][x] == -8){
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
                gridArray[elem.getAttribute("id").split("-")[0]][elem.getAttribute("id").split("-")[1]] = -8;
            }
        }
    }

    function BlankMouseOver(event){
        if(elem.className == "blank"){
            if(isBlankEditable){
                elem.className = "block";
                gridArray[elem.getAttribute("id").split("-")[0]][elem.getAttribute("id").split("-")[1]] = -8;
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
                gridArray[elem.getAttribute("id").split("-")[0]][elem.getAttribute("id").split("-")[1]] = -7;
            }
        }
    }

    function BlockMouseOver(event){
        if(elem.className == "block"){
            if(isBlockEditable){
                elem.className = "blank";
                isBlockChanged = true;
                gridArray[elem.getAttribute("id").split("-")[0]][elem.getAttribute("id").split("-")[1]] = -7;
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
    for (var y = 1; y < height-1; y++) {
        for (var x = 1; x < width-1; x++) {
            
            grida = document.getElementById(y+"-"+x);

            if(gridArray[y][x] == -1){
                grida.className = "start";
            }
            else if(gridArray[y][x] == -2){
                grida.className = "end";
            }
            else if(gridArray[y][x] == -7){
                grida.className = "blank";
            }
            else if(gridArray[y][x] == -8){
                grida.className = "block";
            }
            else if(gridArray[y][x] == -5){
                grida.className = "path";
            }
        }
    }
}

function getOffset(el) {
    const rect = el.getBoundingClientRect();
    return {
      left: rect.left + window.scrollX,
      top: rect.top + window.scrollY
    };
}

function marioDies(){
    anim = document.getElementById("anim");
    mario = document.getElementById("mario");
    mushroom = document.getElementById("mushroom");

    mush_pos = getOffset(document.getElementById("mush"));

    left_pos = mush_pos.left;

    $('#mush').remove();
    $('#mari').remove();

    anim.innerHTML += "<img id='anim-inner' style='position: absolute; bottom: 36px; left: " + left_pos.toString() + "px" + "; height: 144px;' src='../static/lottie/animation1.gif'>";
    mario = document.getElementById("mario");
    mushroom = document.getElementById("mushroom");

    showText("Mario couldn't escaped");

    setTimeout(function(){
        a = left_pos + 68;
        mushroom.innerHTML += "<img id='mush' style='position: absolute; bottom: 36px; left: " + a.toString() +"px;"+ " height: 96px; -webkit-animation: linear infinite; -webkit-animation-name: mushroom-walk-after; -webkit-animation-duration: 5s;' src='../static/lottie/mushroom.gif'></img>";
        setTimeout(function(){
            $("#mush").remove();
        }, 4800);
        $('#anim-inner').remove();
    },2400);
}

function marioLives(){
    mari = document.getElementById("mari");
    mush = document.getElementById("mush");

    mari.style.animationIterationCount = 1;
    mush.style.animationIterationCount = 1;

    fire = document.getElementById("fire");

    fire.style.opacity = "1";
    showText("Mario Escaped");
}

function backToStartAnim(){
    mario = document.getElementById("mario");
    mushroom = document.getElementById("mushroom");

    try{
        $('#mari').remove();
    }catch{}
    try{
        $('#mush').remove();
    }catch{}
    try{
        $('#anim-inner').remove();
    }catch{}
    try{
        $('#aa').remove();
    }catch{}

    mario.innerHTML += "<img id='mari' style='position: absolute; bottom: 36px; left: -44px; height: 72px; -webkit-animation: linear infinite; -webkit-animation-name: mario-walk; -webkit-animation-duration: 7.5s;' src='../static/lottie/mario.gif'>";
    mushroom.innerHTML += "<img id='mush' style='position: absolute; bottom: 36px; left: -172px; height: 96px; -webkit-animation: linear infinite; -webkit-animation-name: mushroom-walk; -webkit-animation-duration: 7.5s;' src='../static/lottie/mushroom.gif'>";

    fire.style.opacity = "0";
}


function updateCanvas(y, x){
    grid = document.getElementById(y + "-" + x);
    grid.className = "path";
}

function showText(txt) {
    $("#text").hide();
    document.getElementById("text").innerHTML = "<a id='aa' style='font-size: 4em;'>"+txt+"</a>";
    $("#text").fadeIn();
}