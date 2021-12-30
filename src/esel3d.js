
class DashBoard {
  constructor(props){
    this.scene = props.scene;
    this.DBisOpen = false;
    this.advancedTexture = BABYLON.GUI.AdvancedDynamicTexture.CreateFullscreenUI("UI");
    this.grid = new BABYLON.GUI.Grid();
    this.gbox = new BABYLON.GUI.Rectangle();
    this.titleGrid = new BABYLON.GUI.Grid();
    this.advancedTexture.addControl(this.gbox);
    this.advancedTexture.addControl(this.grid);
    this.DBcolor = props.worldData.DBColor;
    this.backgroundColor = props.worldData.backgroundColor;
    this.titleWidth = `${props.worldData.titleWidth}px`;
    this.gridWidth = "250px";
    this.gridOpenHeight = "310px";
    this.gboxOpenHeight = "160px";
    this.gridClosedHeight = "30px";
    this.fontSize = "15px";
    this.DBGrid();
    this.TitleGrid();
    this.DBBox();
    this.addColumnRow();
    this.OpenCloseButton();
    this.header();
    this.titleBlock(props.worldData.title);
    
  }
  
  DBGrid(){
    this.grid.background = "transparent";
    this.grid.width = this.gridWidth;
    this.grid.height = this.gridClosedHeight;
    this.grid.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_LEFT;
    this.grid.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;
    this.advancedTexture.addControl(this.grid);
  }

  TitleGrid(){
    this.titleGrid.backgroundColor = this.backgroundColor;
    this.titleGrid.width = this.titleWidth;
    this.titleGrid.height = "30px";
    this.titleGrid.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_RIGHT;
    this.titleGrid.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;
    this.advancedTexture.addControl(this.titleGrid);
  }
  DBBox(){    
    this.gbox.width = this.gridWidth;
    this.gbox.height = this.gridClosedHeight;
    this.gbox.cornerRadius = 2.5;
    this.gbox.alpha = 0.5;
    this.gbox.color = "transparent";
    this.gbox.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_LEFT;
    this.gbox.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;
  }
  addColumnRow(){
    this.grid.addColumnDefinition(150,true);
    this.grid.addColumnDefinition(100, true);  
    this.titleGrid.addColumnDefinition(this.titleWidth, true);
    this.titleGrid.addRowDefinition(30, true);
    this.grid.addRowDefinition(40, true);
    this.grid.addRowDefinition(30, true);
    this.grid.addRowDefinition(30, true);
    this.grid.addRowDefinition(30, true); 
    this.grid.addRowDefinition(30, true);
    this.grid.addRowDefinition(150, true);
  }
  OpenCloseButton(){
    this.tb1 = BABYLON.GUI.Button.CreateImageOnlyButton("tb1", "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCBtZWV0IiB2aWV3Qm94PSIwIDAgNjQwIDY0MCIgd2lkdGg9IjY0MCIgaGVpZ2h0PSI2NDAiPjxkZWZzPjxwYXRoIGQ9Ik01MTEuMjUgNDg5LjYzQzUyMyA1MDEuMzcgNTIzIDUyMC4zOCA1MTEuMjUgNTMyQzUwOC40MyA1MzQuODMgNDg1LjgzIDU1Ny40MiA0ODMgNTYwLjI1QzQ3MS4yNSA1NzIgNDUyLjI1IDU3MiA0NDAuNjMgNTYwLjI1QzQzMi41OCA1NTIuMjIgMzkyLjM4IDUxMi4xIDMyMCA0MzkuODhDMjQ3LjcgNTEyLjE3IDIwNy41MyA1NTIuMzQgMTk5LjUgNTYwLjM4QzE4Ny43NSA1NzIuMTIgMTY4Ljc1IDU3Mi4xMiAxNTcuMTMgNTYwLjM4QzE1NC4yOSA1NTcuNTUgMTMxLjU5IDUzNC45NSAxMjguNzUgNTMyLjEzQzExNyA1MjAuMzggMTE3IDUwMS4zNyAxMjguNzUgNDg5Ljc1QzE0NS43NSA0NzIuNzUgMjgxLjc1IDMzNi43NSAyOTguNzUgMzE5Ljc1QzMxMC41IDMwNy44OCAzMjkuNSAzMDcuODggMzQxLjI1IDMxOS42M0MzNzUuMjUgMzUzLjYzIDQ5NC4yNSA0NzIuNjMgNTExLjI1IDQ4OS42M1pNMTI4Ljc1IDI0OS42M0MxMTcgMjYxLjM4IDExNyAyODAuMzggMTI4Ljc1IDI5MkMxMzEuNTcgMjk0LjgzIDE1NC4xOCAzMTcuNDMgMTU3IDMyMC4yNUMxNjguNzUgMzMyIDE4Ny43NSAzMzIgMTk5LjM4IDMyMC4yNUMyMDcuNDEgMzEyLjIyIDI0Ny41OCAyNzIuMDUgMzE5Ljg4IDE5OS43NUMzOTIuMTcgMjcyLjA1IDQzMi4zNCAzMTIuMjIgNDQwLjM4IDMyMC4yNUM0NTIuMTMgMzMyIDQ3MS4xMyAzMzIgNDgyLjc1IDMyMC4yNUM0ODUuNTggMzE3LjQzIDUwOC4xOCAyOTQuODMgNTExIDI5MkM1MjIuNzUgMjgwLjI1IDUyMi43NSAyNjEuMjUgNTExIDI0OS42M0M0OTQgMjMyLjYzIDM1OCA5Ni42MiAzNDEgNzkuNjJDMzI5LjUgNjcuODcgMzEwLjUgNjcuODcgMjk4Ljc1IDc5LjYyQzI2NC43NSAxMTMuNjMgMTQ1Ljc1IDIzMi42MyAxMjguNzUgMjQ5LjYzWiIgaWQ9ImI0V2pBTUxkVyI+PC9wYXRoPjwvZGVmcz48Zz48Zz48Zz48dXNlIHhsaW5rOmhyZWY9IiNiNFdqQU1MZFciIG9wYWNpdHk9IjEiIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMSI+PC91c2U+PGc+PHVzZSB4bGluazpocmVmPSIjYjRXakFNTGRXIiBvcGFjaXR5PSIxIiBmaWxsLW9wYWNpdHk9IjAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2Utb3BhY2l0eT0iMCI+PC91c2U+PC9nPjwvZz48L2c+PC9nPjwvc3ZnPg==");
    this.tb1.width = "20px";
    this.tb1.height = "20px";
    this.tb1.color = "transparent";
    this.tb1.background = "black";

    this.tb2 = BABYLON.GUI.Button.CreateImageOnlyButton("tb2", "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCBtZWV0IiB2aWV3Qm94PSIwIDAgNjQwIDY0MCIgd2lkdGg9IjY0MCIgaGVpZ2h0PSI2NDAiPjxkZWZzPjxwYXRoIGQ9Ik0xMjguNzUgMTUwLjMyQzExNyAxMzguNTcgMTE3IDExOS41NyAxMjguNzUgMTA3Ljk1QzEzMS41NyAxMDUuMTIgMTU0LjE4IDgyLjUyIDE1NyA3OS43QzE2OC43NSA2Ny45NSAxODcuNzUgNjcuOTUgMTk5LjM4IDc5LjdDMjA3LjQxIDg3LjczIDI0Ny41OCAxMjcuOSAzMTkuODggMjAwLjJDMzkyLjE3IDEyNy45IDQzMi4zNCA4Ny43MyA0NDAuMzggNzkuN0M0NTIuMTMgNjcuOTUgNDcxLjEzIDY3Ljk1IDQ4Mi43NSA3OS43QzQ4NS42IDgyLjUxIDUwOC40IDEwNS4wMSA1MTEuMjUgMTA3LjgyQzUyMyAxMTkuNTcgNTIzIDEzOC41NyA1MTEuMjUgMTUwLjJDNDk0LjI1IDE2Ny4yIDM1OC4yNSAzMDMuMiAzNDEuMjUgMzIwLjJDMzI5LjUgMzMyLjA3IDMxMC41IDMzMi4wNyAyOTguNzUgMzIwLjMyQzI2NC43NSAyODYuMzIgMTQ1Ljc1IDE2Ny4zMiAxMjguNzUgMTUwLjMyWk01MTEuMjUgMzkwLjMyQzUyMyAzNzguNTcgNTIzIDM1OS41NyA1MTEuMjUgMzQ3Ljk1QzUwOC40MyAzNDUuMTIgNDg1LjgzIDMyMi41MiA0ODMgMzE5LjdDNDcxLjI1IDMwNy45NSA0NTIuMjUgMzA3Ljk1IDQ0MC42MyAzMTkuN0M0MzIuNTggMzI3LjcyIDM5Mi4zOCAzNjcuODUgMzIwIDQ0MC4wN0MyNDcuNyAzNjcuNzcgMjA3LjUzIDMyNy42IDE5OS41IDMxOS41N0MxODcuNzUgMzA3LjgyIDE2OC43NSAzMDcuODIgMTU3LjEzIDMxOS41N0MxNTQuMjkgMzIyLjQgMTMxLjU5IDM0NSAxMjguNzUgMzQ3LjgyQzExNyAzNTkuNTcgMTE3IDM3OC41NyAxMjguNzUgMzkwLjJDMTQ1Ljc1IDQwNy4yIDI4MS43NSA1NDMuMiAyOTguNzUgNTYwLjJDMzEwLjUgNTcyLjA3IDMyOS41IDU3Mi4wNyAzNDEuMjUgNTYwLjMyQzM3NS4yNSA1MjYuMzIgNDk0LjI1IDQwNy4zMiA1MTEuMjUgMzkwLjMyWiIgaWQ9ImFoNEpWVGFFUiI+PC9wYXRoPjwvZGVmcz48Zz48Zz48Zz48dXNlIHhsaW5rOmhyZWY9IiNhaDRKVlRhRVIiIG9wYWNpdHk9IjEiIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMSI+PC91c2U+PGc+PHVzZSB4bGluazpocmVmPSIjYWg0SlZUYUVSIiBvcGFjaXR5PSIxIiBmaWxsLW9wYWNpdHk9IjAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2Utb3BhY2l0eT0iMCI+PC91c2U+PC9nPjwvZz48L2c+PC9nPjwvc3ZnPg==");
    this.tb2.width = "20px";
    this.tb2.height = "20px";
    this.tb2.color = "transparent";
    this.tb2.background = "black";
  }
  
  header(){
    var cmdText = new BABYLON.GUI.TextBlock();
    cmdText.text = "Dashboard";
    cmdText.color = this.DBcolor;
    cmdText.fontSize = "15";
    cmdText.fontFamily = "Helvetica";

    this.grid.addControl(this.tb2, 0, 1);           
    this.grid.addControl(cmdText, 0, 0);   
  }

  titleBlock(title){
    var titleText = new BABYLON.GUI.TextBlock();
    titleText.text = title;
    titleText.width = this.titleWidth;
    titleText.backgroundColor = this.backgroundColor;
    titleText.height = "30px";
    titleText.color = this.DBcolor;
    titleText.fontSize = "15";
    titleText.textWrapping = false;
    titleText.fontFamily = "Helvetica";
    this.titleGrid.addControl(titleText, 0);
  }
}

function DBControl(props){
  
  var scene = props.scene;
  var worldData = props.worldData;
  var db = new DashBoard({scene, worldData});
  headerControl(db);
  locatorControl(db);  
  worldControl({db, worldData});

} 



var worldControl = (props) =>{
  var {db, worldData} = props;
  var scene = db.scene;
  const world = new World({scene, worldData})

  var bgText = new BABYLON.GUI.TextBlock();
  bgText.text = "Background Color";
  bgText.color = db.DBcolor;
  bgText.fontSize = "13";
  bgText.fontFamily = "Helvetica"; 

  db.grid.addControl(bgText, 2, 0);

  var pickerText = new BABYLON.GUI.TextBlock();
  pickerText.text = "Open";
  pickerText.color = db.DBcolor;
  pickerText.fontSize = "13";
  pickerText.fontFamily = "Helvetica";

  var pickerEvent = true;
  
  var bgButton = new BABYLON.GUI.Button();
  bgButton.cornerRadius = 2.5
  bgButton.color = db.DBcolor;
  bgButton.addControl(pickerText);
  bgButton.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;
  bgButton.onPointerDownObservable.add(function(){
    if(pickerEvent){
      db.grid.addControl(picker, 5, 0);    
      pickerText.text = "Close"
      pickerEvent = false;
    }
    else{
      db.grid.removeControl(picker, 5, 0);
      pickerText.text = "Open"
      pickerEvent = true;
    }
  })

  db.grid.addControl(bgButton, 2,1);

  var picker = new BABYLON.GUI.ColorPicker();
  picker.value = new BABYLON.Color3(0, 0, 0)
  picker.height = "150px";
  picker.width = "150px";
  picker.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_CENTER;
  picker.onValueChangedObservable.add(function(value) { // value is a color3
      scene.clearColor.copyFrom(value);
  });  

  world.engine.runRenderLoop(function () {
    world.scene.render();
  });

  window.addEventListener("resize", function () {
        world.engine.resize();
  });
}

var locatorControl = (db) =>{
  var scene = db.scene;
  var event = false;
  var {locText, locatorButton, onRadio} = locatorGUI(db.DBcolor);
  db.grid.addControl(locatorButton, 1, 1);
  db.grid.addControl(locText, 1, 0);
  locatorButton.onPointerDownObservable.add(function(){
    if(event){
      onRadio.text = "Off";
      deleteLocator();
      event = false;
    }
    else{
      onRadio.text = "On";
      Locator({scene});      
      event = true;
    }
  })
}

var headerControl = (db) =>{
  var DBisOpen = false
  var collapse = function(){
    if(!DBisOpen){
      db.grid.height = db.gridOpenHeight;
      db.gbox.height = db.gboxOpenHeight;
      db.gbox.color = db.DBcolor;
      db.grid.removeControl(db.tb2);
      db.grid.addControl(db.tb1, 0, 1);
      DBisOpen = true;
    }
    else{      
      db.grid.height = db.gridClosedHeight;
      db.gbox.height = db.gridClosedHeight;
      db.gbox.color = "transparent";
      db.grid.removeControl(db.tb1);
      db.grid.addControl(db.tb2, 0, 1);
      DBisOpen = false;
    }
  }
  
  db.tb1.onPointerDownObservable.add(collapse);
  db.tb2.onPointerDownObservable.add(collapse);
}

var Axis =(props)=> {

  var { scene, size, axisData } = props;

  var makeTextPlane = function(text, color, size) {
  var dynamicTexture = new BABYLON.DynamicTexture("DynamicTexture", 50, scene, true);
  dynamicTexture.hasAlpha = true;
  dynamicTexture.drawText(text, 5, 40, "bold 36px Arial", color , "transparent", true);
  var plane = new BABYLON.Mesh.CreatePlane("TextPlane", size, scene, true);
  plane.material = new BABYLON.StandardMaterial("TextPlaneMaterial", scene);
  plane.material.backFaceCulling = false;
  plane.material.specularColor = new BABYLON.Color3(1, 1, 1);
  plane.material.diffuseTexture = dynamicTexture;
  return plane;
   };
   
   
  var axisX = BABYLON.Mesh.CreateLines("axisX", [ 
    new BABYLON.Vector3.Zero(), new BABYLON.Vector3(size, 0, 0), new BABYLON.Vector3(size * 0.95, 0.05 * size, 0), 
    new BABYLON.Vector3(size, 0, 0), new BABYLON.Vector3(size * 0.95, -0.05 * size, 0)
    ], scene);
  axisX.color = new BABYLON.Color3(1, 0, 0);
  var xChar = makeTextPlane(axisData.xlabel, axisData.xColor, size / 5);
  xChar.position = new BABYLON.Vector3(0.9 * size, 0.1 * size, 0);
  var axisY = BABYLON.Mesh.CreateLines("axisY", [
      new BABYLON.Vector3.Zero(), new BABYLON.Vector3(0, size, 0), new BABYLON.Vector3( -0.05 * size, size * 0.95, 0), 
      new BABYLON.Vector3(0, size, 0), new BABYLON.Vector3( 0.05 * size, size * 0.95, 0)
      ], scene);
  axisY.color = new BABYLON.Color3(0, 1, 0);
  var yChar = makeTextPlane(axisData.ylabel, axisData.yColor, size / 5);
  yChar.position = new BABYLON.Vector3(0, 0.9 * size, 0.1 * size);
  var axisZ = BABYLON.Mesh.CreateLines("axisZ", [
      new BABYLON.Vector3.Zero(), new BABYLON.Vector3(0, 0, size), new BABYLON.Vector3( 0 , -0.05 * size, size * 0.95),
      new BABYLON.Vector3(0, 0, size), new BABYLON.Vector3( 0, 0.05 * size, size * 0.95)
      ], scene);
  axisZ.color = new BABYLON.Color3(0, 0, 1);
  var zChar = makeTextPlane(axisData.zlabel, axisData.zColor, size / 5);
  zChar.position = new BABYLON.Vector3(size, 0.05 * size, 0.9 * size);
 
  
  return [axisX, xChar,
          axisY, yChar,
          axisZ, zChar
        ] 
  }
  class Rect3D {
    constructor(props){
    
      this.scene = props.scene;
      this.solution = props.solution;
      
      this.plotSurface = props.showPlots.plotSurface;
      this.showMinCurve = props.showPlots.showMinCurve;
      this.showMaxCurve = props.showPlots.showMaxCurve;
      this.steps = this.solution.length;
      this.range = this.steps*props.resolution;
      this.indysteps = this.solution[1].length;   
      this.paths = [];
      this.maxCurve = [];
      this.minCurve = [];

      this.drawLines();
      console.log(this.plotSurface)
      if(this.plotSurface === 1){
        this.drawRibbon();
      }
      if(this.showMaxCurve === 1){
        this.drawMaxCurve();
      }
      if(this.showMinCurve === 1){
        this.drawMinCurve();
      }
      
    }
  
    drawLines(){
      
      for(let i = 0; i < this.steps; i++){
        let path = [];
        let tempminmax = [];
        for(let j = 0; j < this.indysteps; j++){
          let x = this.solution[i][j][0];
          let y = this.solution[i][j][1];
          let z = this.solution[i][j][2];
          tempminmax.push(y);
          path.push(new BABYLON.Vector3(x, y, z));
        }
        let maxidx = tempminmax.indexOf(Math.max(...tempminmax));
        let minidx = tempminmax.indexOf(Math.min(...tempminmax));

        this.maxCurve.push(path[maxidx]);
        this.minCurve.push(path[minidx]); 
        this.paths.push(path);
        
        var lines = BABYLON.MeshBuilder.CreateLines("paths",{ points: path});
        lines.alpha = 0.5
        
      }
    }
    
    drawRibbon(){
      const mat = new BABYLON.StandardMaterial("ribbon", this.scene);
      mat.diffuseColor = new BABYLON.Color3(0.5, 0, 0);
      mat.backFaceCulling = false;
      const ribbon = BABYLON.MeshBuilder.CreateRibbon("ribbon", {pathArray: this.paths,
        sideOrientation: BABYLON.Mesh.DOUBLESIDE});
      ribbon.material = mat;
    }
    drawMaxCurve(){
      
      this.maxLine = BABYLON.MeshBuilder.CreateLines("maxline", {points:this.maxCurve});
      var hl = new BABYLON.HighlightLayer("hl1", this.scene);
      hl.addMesh(this.maxLine, BABYLON.Color3.Yellow());
      this.maxLine.edgesWidth = 5;
      
    }
    drawMinCurve(){
      this.minLine = BABYLON.MeshBuilder.CreateLines("minline", {points:this.minCurve});
      var hl = new BABYLON.HighlightLayer("hl1", this.scene);
      hl.addMesh(this.minLine, BABYLON.Color3.Purple());
      this.minLine.outlineWidth = 5;
    }
  }
class World {
  constructor(props){
    
    this.scene = props.scene;
    this.engine = this.scene.getEngine();
    this.canvas = this.scene.getEngine().getRenderingCanvas();
    this.data = props.worldData;
    this.Camera(this.data.cameraDist);
    this.Background(this.data.backgroundColor);
    this.Lighting();

  }

  Camera(cameraDist){
    this.camera = new BABYLON.ArcRotateCamera("ArcRotateCamera", -.85, .8, cameraDist, 
      new BABYLON.Vector3(0, 0, 0), this.scene);
    this.camera.attachControl(this.canvas, true);
    this.camera.wheelPrecision = 10;
  }
  Background(color){
    this.scene.clearColor = color;
  }
  Lighting(){
    var light = new BABYLON.HemisphericLight("light", new BABYLON.Vector3(1, 1, 0));
    light.diffuse = new BABYLON.Color3(1, 1, 1);
  }

  render(){
    
    return;
  }
}

class RectGridClass {
  constructor(props){
    this.scene = props.scene;
    this.xmin = props.gridData.xmin;
    this.ymin = props.gridData.ymin;
    this.zmin = props.gridData.zmin;
    this.xmax = props.gridData.xmax;
    this.ymax = props.gridData.ymax;
    this.zmax = props.gridData.zmax;
    this.alpha = props.gridData.alpha;
    this.gridAlpha = props.gridData.alpha;
    this.numAlpha = 1;
    this.xi = Math.floor(this.xmin);
    this.xf = Math.ceil(this.xmax);
    this.yi = Math.floor(this.ymin);
    this.yf = Math.ceil(this.ymax);
    this.zi = Math.floor(this.zmin);
    this.zf = Math.ceil(this.zmax);
    this.resolution = props.gridData.resolution;
    this.size = 3;
    this.gridColr = props.gridData.gridColor;
    this.axisData = props.gridData.axisData;
    this.xyPlane();
    this.xzPlane();
    this.yzPlane();
    this.xNum();
    this.yNum();
    this.zNum();
    this.showAxis(props.gridData.axisData);
    
  }

  xyPlane(){
    var xy = [];      
    for(let i = this.yi; i <= this.yf; i += this.axisData.yGridStep){
      xy.push([
        new BABYLON.Vector3(this.xi, i, 0),
        new BABYLON.Vector3(this.xf, i, 0)
      ]);
    }
   for(let i = this.xi; i <= this.xf; i += this.axisData.xGridStep){
      xy.push([
        new BABYLON.Vector3(i, this.yi, 0),
        new BABYLON.Vector3(i, this.yf, 0),        
      ]);
    } 
    this.xyGrid = BABYLON.MeshBuilder.CreateLineSystem("xyGrid", {lines:xy}, this.scene);
    this.xyPlanePostition(this.zmax);
    this.xyGrid.alpha = this.alpha;
    this.xyGrid.color = this.gridColr;
  
  }

  xyPlanePostition(zpos){
    this.xyGrid.position = new BABYLON.Vector3(0, 0, zpos);
  }

  xzPlane(){
    var xz = [];
    for(let i = this.xi; i <= this.xf; i += this.axisData.xGridStep){
      xz.push([
        new BABYLON.Vector3(i, 0, this.zi),
        new BABYLON.Vector3(i, 0, this.zf)
      ]);
    }
    for(let i = this.zi; i <= this.zf; i += this.axisData.zGridStep){
      xz.push([
        new BABYLON.Vector3(this.xi, 0, i),
        new BABYLON.Vector3(this.xf, 0, i)
      ]);
    }
    this.xzGrid = BABYLON.MeshBuilder.CreateLineSystem("xzGrid", {lines:xz}, this.scene);
    this.xzGrid.alpha = this.alpha;
    this.xzGrid.color = this.gridColr;
  }

  xzPlanePosition(ypos){
    this.xzGrid.position = new BABYLON.Vector3(0, ypos, 0);
  }

  yzPlane(){
    var yz = [];
    for(let i = this.yi; i <= this.yf; i += this.axisData.yGridStep){
      yz.push([
        new BABYLON.Vector3(0, i, this.zi),
        new BABYLON.Vector3(0, i, this.zf)
      ])
    }
    for(let i = this.zi; i <= this.zf; i += this.axisData.zGridStep){
      yz.push([
        new BABYLON.Vector3(0, this.yi, i),
        new BABYLON.Vector3(0, this.yf, i)
      ]);
    }
    this.yzGrid = BABYLON.MeshBuilder.CreateLineSystem("yzGrid", {lines: yz}, this.scene);
    this.yzGrid.alpha = this.alpha;
    this.yzGrid.color = this.gridColr;
  }

  yzPlanePosition(xpos){
    this.yzGrid.position = new BABYLON.Vector3(xpos, 0, 0)
  }

  makeTextPlane(text, color, size, rotate, axisData){
    var dynamicTexture = new BABYLON.DynamicTexture("text", 50, this.scene, true);
    dynamicTexture.hasAlpha = true;
    dynamicTexture.drawText(text, 10, 40, "15px Arial", color, "transparent", true);
    var plane = BABYLON.Mesh.CreatePlane("textplane", size, this.scene, true);
    var planeMat = new BABYLON.StandardMaterial("textplanematerial", this.scene);
    planeMat.alpha = this.numAlpha;
    planeMat.emissiveColor = new BABYLON.Color3(1, 1, 1);
    planeMat.diffuseColor = new BABYLON.Color3(1, 1, 1);
    plane.material = planeMat;
    if(rotate){ plane.rotation = rotate;};
    plane.material.backFaceCulling = false;
    plane.material.diffuseTexture = dynamicTexture;
    
    return plane;
  }

  countDecimals(num){
    if ((num % 1) != 0) 
        return num.toString().split(".")[1].length;  
    return 0;
  }
  xNum(){
    const decimalPlaces = this.countDecimals(this.axisData.xGridStep)
    for(let i = this.xi; i <= this.xf; i+=this.axisData.xGridStep){
      var xChar = this.makeTextPlane(`${i.toFixed(decimalPlaces)}`, this.axisData.xColor, this.size /5, false);
      xChar.position = new BABYLON.Vector3(i+0.1, 0, -this.axisData.xGridStep/2);
    }
  }
  yNum(){
    const decimalPlaces = this.countDecimals(this.axisData.yGridStep)
    for(let i = this.yi; i <= this.yf; i+=this.axisData.yGridStep){
      if(i===0){continue;}
      var yChar = this.makeTextPlane(`${i.toFixed(decimalPlaces)}`, this.axisData.yColor, this.size /5, false);
      yChar.position = new BABYLON.Vector3( 0, i+0.1, -this.axisData.yGridStep/2);
    }
  }

  zNum(){
    const decimalPlaces = this.countDecimals(this.axisData.zGridStep)
    for(let i = this.zi; i <= this.zf; i+=this.axisData.zGridStep){
      var zChar = this.makeTextPlane(`${i.toFixed(decimalPlaces)}`, this.axisData.zColor, this.size /5, 
        new BABYLON.Vector3(0, -1, 0));
      zChar.position = new BABYLON.Vector3( this.xmax+this.axisData.zGridStep/2, 0, i+0.1);
    }
  }
  hideGrid(){
    this.alpha = 0;
    this.numAlpha = 0;
  }
  showGrid(){
    this.alpha = this.gridAlpha;
    this.numAlpha = 1;
  }

  gridGUI(textColor){
    var gridText = new BABYLON.GUI.TextBlock();
    gridText.text = "Grid Options";
    gridText.color = textColor;
    gridText.fontSize = "18px";
    gridText.fontFamily = "Helvetica";

    var selectText = new BABYLON.GUI.TextBlock();
    selectText.text = "Select";
    selectText.color = textColor;
    selectText.fontSize = "13px";
    selectText.fontFamily = "Helvetica";

    var gridButton = new BABYLON.GUI.Button();
    gridButton.cornerRadius = 2.5
    gridButton.addControl(selectText);
    gridButton.verticalAlignment = BABYLON.Control.VERTICAL_ALIGNMENT_TOP;

    return {gridText, gridButton}
  }

  showAxis(axisData){
    var size = 1;
    var scene = this.scene
    var axis = Axis({scene, size, axisData})
    var axisX = axis[0]
    var xChar = axis[1]
    var axisY = axis[2]
    var yChar = axis[3]
    var axisZ = axis[4] 
    var zChar = axis[5] 
    axisX.scaling.x = this.xf;
    axisY.scaling.y = this.yf;
    axisZ.scaling.z = this.zf;
    xChar.scaling.x = 2;
    xChar.scaling.y = 2;
    xChar.position.x = this.xf + .5;
    yChar.scaling.x = 2;
    yChar.scaling.y = 2;
    yChar.position.y = this.yf + .5;
    zChar.scaling.x = 2;
    zChar.scaling.y = 2;
    zChar.position.x = this.xf + .5;
    zChar.position.z = this.zf + .5;
  }

  getAlpha(){
    return this.alpha;
  }
  setAlpha(a){
    this.alpha = a;
  }
  render(){
    return 
  }
}

class locatorClass {
  constructor(props){
    this.color = "white";
    this.scene = props.scene;    
    this.ballMat = new BABYLON.StandardMaterial("locator", this.scene);
    this.ball = new BABYLON.MeshBuilder.CreateSphere("locator",
      {diameter: 0.10}, this.scene);       
    this.utilLayer = new BABYLON.UtilityLayerRenderer(this.scene);
    this.gizmo = new BABYLON.PositionGizmo(this.utilLayer);
    this.advancedTexture = BABYLON.GUI.AdvancedDynamicTexture.CreateFullscreenUI("UI");
    this.label = new BABYLON.GUI.TextBlock();
    this.rect1 = new BABYLON.GUI.Rectangle();
    
    this.Ball();    
    this.Gizmo();    
    this.Coords();
  }

  Ball(){
    this.ballMat.diffuseColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    this.ballMat.specularColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    this.ballMat.emissiveColor = BABYLON.Color3.Yellow();
    this.ball.material = this.ballMat;    
  }
  Gizmo(){
    this.gizmo.attachedMesh = this.ball;
    this.gizmo.scaleRatio = 0.75;
    this.gizmo.updateGizmoRotationToMatchAttachedMesh = false;
    this.gizmo.updateGizmoPositionToMatchAttachedMesh = true;
  }
  
  Coords(){
    this.rect1.width = "0.5em";
    this.rect1.height = "30px";
    this.rect1.cornerRadius = 20;
    this.rect1.color = "transparent";
    this.rect1.thickness = 0.5;
    this.rect1.background = "transparent";
    this.advancedTexture.addControl(this.rect1);
    this.rect1.linkWithMesh(this.ball);
    this.rect1.linkOffsetY = -150;

    this.label.text = "X: U: T: ";
    this.label.fontSize = "15px";
    this.label.color = this.color;
    this.rect1.addControl(this.label);          
  }

  delete(){
    this.ball.dispose();
    this.ballMat.dispose();
    this.gizmo.dispose();
    this.label.dispose();
    this.rect1.dispose();
  }
  render(){       

    document.onkeydown = ()=>{      
      this.gizmo.attachedMesh = !this.gizmo.attachedMesh ? this.ball : null  
    }
    return;
    
  }
}
let c;
function Locator(props){
  var { scene } = props;
  c = new locatorClass({scene});
  scene.onPointerObservable.add(function(){
    var coords = c.ball.getPositionExpressedInLocalSpace();
    c.label.text = "X: "+coords._x.toFixed(2).toString()+" "+
      " U: "+coords._y.toFixed(2).toString()+" "+
      " T: "+coords._z.toFixed(2).toString();
  })
}

function deleteLocator(){
  if(c){
    c.delete();
  }
}

function locatorGUI(textColor){
  var locText = new BABYLON.GUI.TextBlock();
  locText.text = "Point Explorer";
  locText.color = textColor;
  locText.fontSize = "13";
  locText.fontFamily = "Helvetica";
  locText.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;
  locText.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_LEFT;

  var onRadio = new BABYLON.GUI.TextBlock();
  onRadio.text = "Off";
  onRadio.color = textColor;
  onRadio.fontSize = "13";
  onRadio.fontFamily = "Helvetica";
  onRadio.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;

  var locatorButton = new BABYLON.GUI.Button();
  locatorButton.cornerRadius = 2.5;
  locatorButton.color = textColor;
  locatorButton.addControl(onRadio);
  locatorButton.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;

  return {locText, locatorButton, onRadio};
}
export {DBControl, Axis, World, RectGridClass, Rect3D, locatorClass };