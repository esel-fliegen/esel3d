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
         <script src="https://preview.babylonjs.com/gui/babylon.gui.min.js"></script>
        <script src="https://preview.babylonjs.com/materialsLibrary/babylonjs.materials.min.js"></script>
        <script src="https://preview.babylonjs.com/proceduralTexturesLibrary/babylonjs.proceduralTextures.min.js"></script>
        <script src="https://preview.babylonjs.com/postProcessesLibrary/babylonjs.postProcess.min.js"></script>
        <script src="https://preview.babylonjs.com/loaders/babylonjs.loaders.js"></script>
        <script src="https://preview.babylonjs.com/serializers/babylonjs.serializers.min.js"></script>
       

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
        <script src="https://preview.babylonjs.com/gui/babylon.gui.min.js"></script>
        <script type="module">
            
        import {DBControl, Axis, World, RectGridClass, Rect3D, locatorClass} from 'https://cdn.jsdelivr.net/gh/esel-fliegen/esel3d@0.1.42/src/esel3d/esel3d.js';
        
            var canvas = document.getElementById("renderCanvas");
            const engine = new BABYLON.Engine(canvas, true);  
            const scene = new BABYLON.Scene(engine);

            const Data = %s;
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
            
            for(let i = 0; i < Data.solution.length; i++){
                showPlots.surfaceColor = [0, 0, 0];
                showPlots.surfaceColor[i] = 0.5;
                const solution = Data.solution[i];
                var curve = new Rect3D({scene, solution, plotResolution, showPlots});
            }

            var db = DBControl({scene, worldData});
        </script>
		""" % str(x)
  )




class plot3d:
    """
    Main injection class for esel3D
    
    Attributes (all private and has default values)
    ----------
    title : string
        default "ESEL3D"
    xinitial : number
        minimum value of x
        default = 0
    xfinal : number
        maximum value of x
        default = 0
    yinitial : number
        minimum value of y
        default = 0
    yfinal : number
        maximum value of y
        default = 0
    xDomain : number
        xfinal - xinitial
        default = 0
    yDomain : number
        yfinal - yinitial
        default = 0
    plotResolution : number
        resolution or step of the lines or surface
        default = 1
    solution : list
        all the points/vertices to be plotted
        default = []
    maxCurve : list
        the maximun curve of the plot
        default = []
    minCurve : list
        the minimum curve of the plot
        default = []
    showMaxCurve : int
        display the max curve on the plot
        default = 0 (set to 1 to show)
    showMinCurve : int
        display the min curve on the plot
        default = 0 (set to 1 to show)
    plotSurface : int
        display the surface plot
        default = 0 (however the surface() method will default this to 1)
    plotLine : int
        display the line plot
        default = 0 (however the surface() method will default this to 1)
    theme : string
        dark or light theme
        default = "dark"
    xLabel : string
        display the x-axis label
        default = "X"
    yLabel : string
        display the y-axis label
        default = "Y"
    zLabel : string
        display the z-axis label
        default = "Z"
    xColor : string
        color theme for the x-axis
        default = "red"
    yColor : string
        color theme for the y-axis 
        Note: the y and z axis on the BabylonJS are switched
        default = "green"
    zColor : string
        color theme for the z-axis 
        Note: the y and z axis on the BabylonJS are switched
        default = "blue"
    xGridStep : number
        tick resolution for the x-axis
        default = 1
    yGridStep : number
        tick resolution for the y-axis
        default = 1
    zGridStep : number
        tick resolution for the z-axis
        default = 1
    
    Methods
    -------

    plot()
        Retrieve parameters and plot.
    xAxis(**kwwarg)
        Set xLabel, xColor and xGridStep.    
    yAxis(**kwarg)
        Set yLabel, yColor and yGridStep.
    zAxis(**kwarg)
        Set zLabel, zColor and zGridStep.
    surface(func, x, y, resolution, **kwargs)
        Assemble parameters for surface plot.
    theme(theme)
        Set the theme for the plot
    title(title="ESEL3D")
        Set title for the plot.
    getParameters()
        Retrieve all parameters to be plotted.
    initData(func)
        Calculate and populate solution from parameters and function.
    
    """


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
        self.__surfaceColor = []
        self.__xGridStep=1
        self.__yGridStep=1
        self.__zGridStep=1
        self.__data = {}
        display(HTML(self.__bg.header()))

    def __del__(self):
        print("plot3d deleted.")
    
    def plot(self):
        """Retrieve parameters, default or user defined, and plot the graph."""
        self.getParameters()
        display(HTML(self.__bg.scene(self.__data)))

    def theme(self, theme="dark"):
        """
        Set the theme for the plot.

        Parameter
        ---------

        theme : string
            Only "dark" and "light" are available.
            default = "dark"
        """
        self.__theme = theme

    def xAxis(self, **kwargs):
        """
        Set parameters for x-axis

        Parameters
        ----------

        xLabel : string
            Label for the x-axis
            default = "X"
        xColor : string
            color theme for the x-axis
            default = "red"        
        xGridStep : number
            tick resolution for the x-axis
            default = 1        
        """
        if kwargs.get('xLabel') != None:
            self.__xlabel = kwargs.get('xLabel')
        if kwargs.get('xColor') !=None:
            self.__xColor = kwargs.get('xColor')
        if kwargs.get('xGridStep') != None:
            self.__xGridStep = kwargs.get('xGridStep')

    def yAxis(self, **kwargs):
        """
        Set parameters for y-axis
        Note: the y and z axis are switched in BabylonJS

        Parameters
        ----------

        yLabel : string
            Label for the y-axis
            default = "Y"
        yColor : string
            color theme for the y-axis
            default = "green"        
        yGridStep : number
            tick resolution for the y-axis
            default = 1        
        """
        if kwargs.get('yLabel') != None:
            self.__zlabel = kwargs.get('yLabel')
        if kwargs.get('yColor') !=None:
            self.__zColor = kwargs.get('yColor')
        if kwargs.get('yGridStep') != None:
            self.__zGridStep = kwargs.get('yGridStep')

    def zAxis(self, **kwargs):
        """
        Set parameters for z-axis
        Note: the y and z axis are switched in BabylonJS

        Parameters
        ----------

        zLabel : string
            Label for the z-axis
            default = "Z"
        zColor : string
            color theme for the z-axis
            default = "blue"        
        zGridStep : number
            tick resolution for the z-axis
            default = 1        
        """
        if kwargs.get('zLabel') != None:
            self.__ylabel = kwargs.get('zLabel')
        if kwargs.get('zColor') !=None:
            self.__yColor = kwargs.get('zColor')
        if kwargs.get('zGridStep') != None:
            self.__yGridStep = kwargs.get('zGridStep')


    def surface(self, func, x, y, resolution, plotLines = 1, plotSurface = 1, **kwargs):
        """
        Assemble the function and parameters for a surface plot.

        Parameters
        ----------

        func : function
            User defined function that takes two parameters
        x : list
            Parameters for the x domain.
        y : list
            Parameters for the y domain.
        z : list
            Parameters for the z domain.
        resolution : number
            Surface resolution or step.
        **kwargs : string
            showMaxCurve and showMinCurve.
        
        """
        
        self.__xinitial = min(self.__xinitial, x[0])
        self.__xfinal = max(self.__xfinal, x[1])
        self.__xDomain = max((self.__xfinal - self.__xinitial), self.__xDomain)
        
        self.__yinitial = min(self.__yinitial, y[0])
        self.__yfinal = max(self.__yfinal, y[1])
        self.__yDomain = max((self.__yfinal - self.__yinitial), self.__yDomain)

        self.__plotResolution = resolution
        if kwargs.get('showMaxCurve') != None:
            self.__showMaxCurve = kwargs.get('showMaxCurve')
        if kwargs.get('showMinCurve') != None:
            self.__showMinCurve = kwargs.get('showMinCurve')
        self.__plotLines = plotLines 
        self.__plotSurface = plotSurface
        self.initData(func, x , y)
               
    def title(self, title = "ESEL3D"):
        """
        Set plot title.

        Parameter
        ---------
        
        title : string
            default = "ESEL3D"
        """
        self.__title = title

    def getParameters(self):
        """
        Retrieve all parameters as dictionary.

        """
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
                "surfaceColor":self.__surfaceColor,
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

    def initData(self, func, x = None, y = None):
        """
        Assemble the solution list from the function and parameters.

        """
        xDomain = x[1] - x[0]
        yDomain = y[1] - y[0]
        dx = np.linspace(x[0], x[1], int(xDomain/self.__plotResolution+1))
        dy = np.linspace(y[0], y[1], int(yDomain/self.__plotResolution+1))     
        tempSolution = []
        try:
          for i in dy:
              z = func(dx, i)
              p = np.array(list(zip(dx, z, np.full((int(xDomain/self.__plotResolution+1),), i))))
              temp = []
              for j in p:
                  temp.append(j[1])
                  self.__range.append(j[1])
              self.__maxCurve.append(p[temp.index(max(temp))].tolist())
              self.__minCurve.append(p[temp.index(min(temp))].tolist())
              tempSolution.append(p.tolist())
        except TypeError:
          for i in dx:
              z = func(i, dy)
              p = np.array(list(zip(z, dy, np.full((int(yDomain/self.__plotResolution+1),), i))))
              temp = []
              for j in p:
                  temp.append(j[1])
                  self.__range.append(j[1])
              self.__maxCurve.append(p[temp.index(max(temp))].tolist())
              self.__minCurve.append(p[temp.index(min(temp))].tolist())
              tempSolution.append(p.tolist())
        self.__solution.append(tempSolution)
        if max(self.__range) > self.__maxPoint:
            self.__maxPoint = max(self.__range)
        if min(self.__range) < self.__minPoint:
            self.__minPoint = min(self.__range)
        

