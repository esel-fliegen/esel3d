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
            resolution: Data.gridStep,
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




class plot3d:
    def __init__(self):
        self.bg = BLoader()       
        self.title="ESEL3D"
        self.xinitial=0
        self.xfinal=0
        self.yinitial=0
        self.yfinal=0
        self.x=0
        self.y=0
        self.resolution=1
        self.gridStep=1
        self.solution=[]
        self.maxCurve = []
        self.minCurve = []
        self.range = []
        self.maxPoint=0
        self.minPoint=0
        self.theme="dark"
        self.xlabel="X"
        self.ylabel="Y"
        self.zlabel="Z"
        self.xColor="red"
        self.yColor="green"
        self.zColor="blue"
        self.data = {}
        display(HTML(self.bg.header()))
    
    def plot(self):
        self.get_parameters()
        display(HTML(self.bg.scene(self.data)))

    def surface(self, func, x, xi, xf, y, yi, yf, resolution):
        self.x = x
        self.xi = xi
        self.xf = xf
        self.y = y 
        self.yi = yi 
        self.yf = yf 
        self.resolution = resolution
                
        self.init_data(func)
        print(self.solution)
               

    def get_parameters(self):
        self.data = {
            "title":self.title,
            "xinitial":self.xinitial,
            "xfinal":self.xfinal,
            "yinitial":self.yinitial,
            "yfinal":self.yfinal,
            "x":self.x,
            "y":self.y,
            "resolution":self.resolution,
            "gridStep":self.gridStep,
            "solution":self.solution,
            "maxPoint":self.maxPoint,
            "minPoint":self.minPoint,
            "theme":self.theme,
            "axisConfig":{
                "xlabel":self.xlabel,
                "ylabel":self.ylabel,
                "zlabel":self.zlabel,
                "xColor":self.xColor,
                "yColor":self.yColor,
                "zColor":self.zColor,
            }            
        }

    def init_data(self, func):
        dx = np.linspace(self.xi, self.xf, int(self.x/self.resolution+1))
        dy = np.linspace(self.yi, self.yf, int(self.y/self.resolution+1))        

        for i in dy:
            z = func(dx, i)
            p = np.array(list(zip(dx, z, np.full((int(self.x/self.resolution),), i))))
            temp = []
            for j in p:
                temp.append(j[1])
                self.range.append(j[1])
            self.maxCurve.append(p[temp.index(max(temp))].tolist())
            self.minCurve.append(p[temp.index(min(temp))].tolist())
            self.solution.append(p.tolist())
        self.maxPoint = max(self.range)
        self.minPoint = min(self.range)
        

