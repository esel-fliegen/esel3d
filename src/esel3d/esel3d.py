from IPython.core.display import display
from IPython.display import HTML

import numpy as np

class BLoader:
    def __init__(self, backgroundColor=(1, 1, 1)):
        self.backgroundColor = backgroundColor

    def __header(self):
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

    def __scene(self, x):
	    return(
		"""
		<canvas id="renderCanvas"></canvas>
        <script src="https://preview.babylonjs.com/gui/babylon.gui.min.js"></script>
        <script type="module">
            
        import {DBControl, Axis, World, RectGridClass, Rect3D, locatorClass} from 'https://cdn.jsdelivr.net/gh/esel-fliegen/esel3d@0.1.48/src/esel3d/esel3d.js';
        
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
                delete Data.solution[i];
            }

            var db = DBControl({scene, worldData});
        </script>
		""" % str(x)
  )




class plot3d(BLoader):
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
    __getParameters()
        Retrieve all parameters to be plotted.
    setGrid(x-initial, x-final, y-initial, y-final, z-initial, z-final)
        Set grid parameters after surface creation.  
    initData(func)
        Calculate and populate solution from parameters and function.
    initData2(func)
        Calculate and populate solution from multiple functions.
    
    """


    def __init__(self):
             
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
        self.__ylabel="Y"
        self.__zlabel="Z"
        self.__xColor="red"
        self.__yColor="green"
        self.__zColor="blue"
        self.__surfaceColor = []
        self.__xGridStep=1
        self.__yGridStep=1
        self.__zGridStep=1
        self.__data = {}
        display(HTML(self._BLoader__header()))

    def __del__(self):
        print("plot3d deleted.")
    
    def plot(self):
        """Retrieve parameters, default or user defined, and plot the graph."""
        self.__getParameters()
        display(HTML(self._BLoader__scene(self.__data)))
        del self.__solution

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
            self.__ylabel = kwargs.get('yLabel')
        if kwargs.get('yColor') !=None:
            self.__yColor = kwargs.get('yColor')
        if kwargs.get('yGridStep') != None:
            self.__yGridStep = kwargs.get('yGridStep')

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
            self.__zlabel = kwargs.get('zLabel')
        if kwargs.get('zColor') !=None:
            self.__zColor = kwargs.get('zColor')
        if kwargs.get('zGridStep') != None:
            self.__zGridStep = kwargs.get('zGridStep')


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
        if type(func)==list:
          self.initData2(func, x, y)
        else:
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

    def setSolution(self, solution):
        """
        Manually set solution to plot.

        Parameter
        ---------

        solution = list
            four dimensional list

            i.e.
            [[[[x, y, z],...,[x, y, z]]]]
            solution set -> surface -> lines -> points

        """
        self.__solution = solution

    def setGrid(self, xi, xf, yi, yf, zi, zf):
        """
        Set grid parameters after surface creation. 

        Parameter
        ---------

        xi = number
        xf = number
        yi = number
        yf = number
        zi = number
        zf = number
        """
        self.__xinitial = xi
        self.__xfinal = xf
        self.__yinitial = yi
        self.__yfinal = yf
        self.__minPoint = zi
        self.__maxPoint = zf

    def setData(self, data):
        """
        Manually insert data parameters.

        Parameter
        ---------

        data : dictionary
            all data parameters
        """
        self.__title = data.get("title")
        self.__xinitial = data.get("xinitial")
        self.__xfinal = data.get("xfinal")
        self.__yinitial = data.get("yinitial")
        self.__yfinal = data.get("yfinal")
        self.__xDomain = data.get("xdomain")
        self.__yDomain = data.get("ydomain")
        self.__surfaceColor = data.get("plots").get("surfaceColor")
        self.__showMaxCurve = data.get("plots").get("showMaxCurve")
        self.__showMinCurve = data.get("plots").get("showMinCurve")
        self.__plotLines = data.get("plots").get("plotLines")
        self.__plotSurface = data.get("plots").get("plotSurface")
        self.__solution = data.get("solution")
        self.__maxPoint = data.get("maxPoint")
        self.__minPoint = data.get("minPoint")
        self.__theme = data.get("theme")
        self.__xlabel = data.get("axisConfig").get("xlabel")
        self.__ylabel = data.get("axisConfig").get("ylabel")
        self.__zlabel = data.get("axisConfig").get("zlabel")
        self.__xColor = data.get("axisConfig").get("xColor")
        self.__yColor = data.get("axisConfig").get("yColor")
        self.__zColor = data.get("axisConfig").get("zColor")
        self.__xGridStep = data.get("axisConfig").get("xGridStep")
        self.__yGridStep = data.get("axisConfig").get("yGridStep")
        self.__zGridStep = data.get("axisConfig").get("zGridStep")


    def printParams(self):
        """
        Prints plot parameters.
        """
        print("Title: ", self.__title)
        print("X-initial: ", self.__xinitial)
        print("X-final: ", self.__xfinal)
        print("Y-initial: ", self.__yinitial)
        print("Y-final: ", self.__yfinal)
        print("X-domain: ", self.__xDomain)
        print("Y-domain: ", self.__yDomain)
        print("Plot resolution: ", self.__plotResolution)
        print("Theme: ", self.__theme)
        print("X-label: ", self.__xlabel)
        print("X-color: ", self.__xColor)
        print("X-step: ", self.__xGridStep)
        print("Y-label: ", self.__ylabel)
        print("Y-color: ", self.__yColor)
        print("Y-step: ", self.__yGridStep)
        print("Z-label: ", self.__zlabel)
        print("Z-color: ", self.__zColor)
        print("Z-step: ", self.__zGridStep)


    def __getParameters(self):
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

    def initData2(self, func, x = None, y = None):
        """
        Assemble the a list of solution list from the function and parameters. 
        X and Y and independent variable and Z is dependent. 
        """
        xDomain = x[1] - x[0]
        yDomain = y[1] - y[0]
        dx = np.linspace(x[0], x[1], int(xDomain/self.__plotResolution+1))
        dy = np.linspace(y[0], y[1], int(yDomain/self.__plotResolution+1))     
        tempSolution = []
        for f in func:
            try:
                for i in dy:
                    z = f(dx, i)
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
                    z = f(i, dy)
                    p = np.array(list(zip(np.full((int(yDomain/self.__plotResolution+1),), i), dy, z)))
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


    def initData(self, func, x = None, y = None):
        """
        Assemble the solution list from the function and parameters. 
        X and Y and independent variable and Z is dependent. 
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
              p = np.array(list(zip(np.full((int(yDomain/self.__plotResolution+1),), i), dy, z)))
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
        

