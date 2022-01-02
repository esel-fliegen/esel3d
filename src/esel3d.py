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
            
        import {DBControl, Axis, World, RectGridClass, Rect3D, locatorClass} from 'https://cdn.jsdelivr.net/gh/esel-fliegen/esel3d@0.1.31/src/esel3d.js';
        
            var canvas = document.getElementById("renderCanvas");
            const engine = new BABYLON.Engine(canvas, true);  
            const scene = new BABYLON.Scene(engine);

            const Data = %s;
            const solution = Data.solution;
            const plotResolution = Data.plotResolution;
            const showPlots = Data.plots;

            var gridColor = new BABYLON.Color3(1, 1, 1);
            var bgColor = new BABYLON.Color3(0,0,0);
            var dbColor = "yellow";

            if(Data.theme==="light"){
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
  
            var grid = new RectGridClass({scene,gridData});  
            var curve = new Rect3D({scene, solution, plotResolution, showPlots});
            var db = DBControl({scene, worldData});
        </script>
		""" % str(x)
  )




class plot3d:
    def __init__(self):
        self.__bg = BLoader()       
        self.__title="ESEL3D"
        self.__xinitial=0
        self.__xfinal=0
        self.__yinitial=0
        self.__yfinal=0
        self.__xDomain=0
        self.__yDomain=0
        self.__plotResolution=1
        self.__solution=[]
        self.__maxCurve = []
        self.__minCurve = []
        self.__showMaxCurve = 0
        self.__showMinCurve = 0 
        self.__plotSurface = 0 
        self.__plotLines = 0         
        self.__range = []
        self.__maxPoint=0
        self.__minPoint=0
        self.__theme="dark"
        self.__xlabel="X"
        self.__ylabel="Z"
        self.__zlabel="Y"
        self.__xColor="red"
        self.__yColor="green"
        self.__zColor="blue"
        self.__xGridStep=1
        self.__yGridStep=1
        self.__zGridStep=1
        self.__data = {}
        display(HTML(self.__bg.header()))
    
    def plot(self):
        self.get_parameters()
        display(HTML(self.__bg.scene(self.__data)))

    def xAxis(self, **kwargs):

        if kwargs.get('xLabel') != None:
            self.__xlabel = kwargs.get('xLabel')
        if kwargs.get('xColor') !=None:
            self.__xColor = kwargs.get('xColor')
        if kwargs.get('xGridStep') != None:
            self.__xGridStep = kwargs.get('xGridStep')

    def yAxis(self, **kwargs):
        if kwargs.get('yLabel') != None:
            self.__zlabel = kwargs.get('yLabel')
        if kwargs.get('yColor') !=None:
            self.__zColor = kwargs.get('yColor')
        if kwargs.get('yGridStep') != None:
            self.__zGridStep = kwargs.get('yGridStep')

    def theme(self, theme):
        self.__theme = theme

    def zAxis(self, **kwargs):
        if kwargs.get('zLabel') != None:
            self.__ylabel = kwargs.get('zLabel')
        if kwargs.get('zColor') !=None:
            self.__yColor = kwargs.get('zColor')
        if kwargs.get('zGridStep') != None:
            self.__yGridStep = kwargs.get('zGridStep')


    def surface(self, func, x, y, resolution, **kwargs):
        self.__xDomain = x[0]
        self.__xinitial = x[1]
        self.__xfinal = x[2]
        self.__yDomain = y[0] 
        self.__yinitial = y[1]
        self.__yfinal = y[2]
        self.__plotResolution = resolution
        if kwargs.get('showMaxCurve') != None:
            self.__showMaxCurve = kwargs.get('showMaxCurve')
        if kwargs.get('showMinCurve') != None:
            self.__showMinCurve = kwargs.get('showMinCurve')
        self.__plotLines = 1 
        self.__plotSurface = 1
        self.init_data(func)
               

    def get_parameters(self):
        self.__data = {
            "title":self.__title,
            "xinitial":self.__xinitial,
            "xfinal":self.__xfinal,
            "yinitial":self.__yinitial,
            "yfinal":self.__yfinal,
            "x":self.__xDomain,
            "y":self.__yDomain,
            "plotResolution":self.__plotResolution,
            "plots":{
                "showMaxCurve":self.__showMaxCurve,
                "showMinCurve":self.__showMinCurve,
                "plotLines":self.__plotLines,
                "plotSurface":self.__plotSurface,
            },
            "solution":self.__solution,
            "maxPoint":self.__maxPoint,
            "minPoint":self.__minPoint,
            "theme":self.__theme,
            "axisConfig":{
                "zmin":self.__yinitial,
                "xlabel":self.__xlabel,
                "ylabel":self.__ylabel,
                "zlabel":self.__zlabel,
                "xColor":self.__xColor,
                "yColor":self.__yColor,
                "zColor":self.__zColor,
                "xGridStep":self.__xGridStep,
                "yGridStep":self.__yGridStep,
                "zGridStep":self.__zGridStep,
            }            
        }

    def init_data(self, func):
        dx = np.linspace(self.__xinitial, self.__xfinal, int(self.__xDomain/self.__plotResolution+1))
        dy = np.linspace(self.__yinitial, self.__yfinal, int(self.__yDomain/self.__plotResolution+1))        

        for i in dy:
            z = func(dx, i)
            p = np.array(list(zip(dx, z, np.full((int(self.__xDomain/self.__plotResolution+1),), i))))
            temp = []
            for j in p:
                temp.append(j[1])
                self.__range.append(j[1])
            self.__maxCurve.append(p[temp.index(max(temp))].tolist())
            self.__minCurve.append(p[temp.index(min(temp))].tolist())
            self.__solution.append(p.tolist())
        self.__maxPoint = max(self.__range)
        self.__minPoint = min(self.__range)
        

