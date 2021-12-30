from IPython.core.display import display
from IPython.display import HTML

import numpy as np

class BLoader:
    def __init__(self, backgroundColor=(1, 1, 1)):
        self.backgroundColor = backgroundColor

    def header(self):
        return("""
		<head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

        <script src="https://preview.babylonjs.com/babylon.js"></script>
        <script src="https://preview.babylonjs.com/materialsLibrary/babylonjs.materials.min.js"></script>
        <script src="https://preview.babylonjs.com/proceduralTexturesLibrary/babylonjs.proceduralTextures.min.js"></script>
        <script src="https://preview.babylonjs.com/postProcessesLibrary/babylonjs.postProcess.min.js"></script>
        <script src="https://preview.babylonjs.com/loaders/babylonjs.loaders.js"></script>
        <script src="https://preview.babylonjs.com/serializers/babylonjs.serializers.min.js"></script>
        <script src="https://preview.babylonjs.com/gui/babylon.gui.min.js"></script>

        <style>
            html, body {
            overflow: hidden;
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            }

            #renderCanvas {
            width: 100%;
            height: 100%;
            touch-action: none;
                }
        </style>
        </head>
  """)

    def scene(self, x):
	    return(
		"""
		<canvas id="renderCanvas"></canvas>
      
        <script type="module">
            
        import {DBControl, Axis, World, RectGridClass, Rect3D, locatorClass} from 'https://cdn.jsdelivr.net/gh/esel-fliegen/esel3d@0.1.6/src/esel3d.js';
        
            var canvas = document.getElementById("renderCanvas");
            const engine = new BABYLON.Engine(canvas, true);  
            const scene = new BABYLON.Scene(engine);

            const Data = %s;
            const solution = Data.solution;
            const resolution = Data.resolution;

            var gridColor = new BABYLON.Color3(1, 1, 1);
            var bgColor = new BABYLON.Color3(0,0,0);
            var dbColor = "yellow";

            if(Data.backgroundColor==="light"){
            gridColor = new BABYLON.Color3(0, 0, 0);
            bgColor = new BABYLON.Color3(1, 1, 1);
            dbColor = "black";
            }

            const gridData = {
            xmin: Data.xinitial,
            ymin: Data.minPoint,
            zmin: Data.yinitial,
            xmax: Data.xfinal,
            ymax: Data.maxPoint,
            zmax: Data.yfinal,
            resolution: resolution,
            alpha: 0.5,
            gridColor: gridColor,
            axisData: Data.axisConfig,
            }
            const dz = Data.yfinal - Data.yinitial;

            const worldData = {
            cameraDist: dz,
            backgroundColor: bgColor,
            DBColor:dbColor,
            title:Data.title,
            titleWidth:Data.title.length * 12.5,
            }
            console.log
            var grid = new RectGridClass({scene,gridData});  
            var curve = new Rect3D({scene, solution, resolution});
            var db = DBControl({scene, worldData});
        </script>
		""" % str(x)
  )




class plot:
    def __init__(self):
        self.bg = BLoader()       

        display(HTML(self.bg.header()))
        
    
    def surface(self, func, x, xi, xf, y, yi, yf, resolution):
        soln, maxCurve, minCurve, range, zMax, zMin = init_data(func, x, xi, xf, y, yi, yf, resolution)
        data = get_parameters(xinitial=xi, xfinal=xf, yinitial=yi, 
            yfinal=yf,x=x,y=y,resolution=resolution,maxPoint=zMax,minPoint=zMin, solution=soln)
        display(HTML(self.bg.scene(data)))

def init_data(func, x, xi, xf, y, yi, yf, resolution):
    dx = np.linspace(xi, xf, int(x/resolution+1))
    dy = np.linspace(yi, yf, int(y/resolution+1))

    soln = []
    maxCurve = []
    minCurve = []
    range = []

    for i in dy:
        z = func(dx, i)
        p = np.array(list(zip(dx, z, np.full((int(x/resolution),), i))))
        temp = []
        for j in p:
            temp.append(j[1])
            range.append(j[1])
        maxCurve.append(p[temp.index(max(temp))].tolist())
        minCurve.append(p[temp.index(min(temp))].tolist())
        soln.append(p.tolist())
    zMax = max(range)
    zMin = min(range)
    return soln, maxCurve, minCurve, range, zMax, zMin

def get_parameters(
    title="ESEL3D",
    xinitial=0,
    xfinal=0,
    yinitial=0,
    yfinal=0,
    x=0,
    y=0,
    resolution=1,
    solution=[],
    maxPoint=0,
    minPoint=0,
    theme="dark",
    xlabel="X",
    ylabel="Y",
    zlabel="Z",
    xColor="red",
    yColor="blue",
    zColor="green",
    ):
    data = {
        "title":title,
        "xinitial":xinitial,
        "xfinal":xfinal,
        "yinitial":yinitial,
        "yfinal":yfinal,
        "x":x,
        "y":y,
        "resolution":resolution,
        "solution":solution,
        "maxPoint":maxPoint,
        "minPoint":minPoint,
        "theme":theme,
        "axisConfig":{
            "xlabel":xlabel,
            "ylabel":ylabel,
            "zlabel":zlabel,
            "xColor":xColor,
            "yColor":yColor,
            "zColor":zColor,
        }
        
    }
    return data